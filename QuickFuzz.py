import requests
import argparse
import sys
from concurrent.futures import ThreadPoolExecutor
import signal
import os

def graceful_exit(sig, frame):
    print("\n[!] Exiting gracefully...")
    os._exit(0)

signal.signal(signal.SIGINT, graceful_exit)

parser = argparse.ArgumentParser(description="HTTP Directory Fuzzer")

parser.add_argument('-u', '--url', type=str, required=True, help='Base URL to fuzz')
parser.add_argument('-w', '--wordlist', type=str, required=True, help='Path to the wordlist file')

args = parser.parse_args()

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

response = requests.get(args.url, headers=headers)
if response.status_code != 200:
    print(f"[!] Error: Unable to reach {args.url}. Status code: {response.status_code}")
    sys.exit(1)

def fuzz_directory(args, word):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    try:
        response = requests.get(f"{args.url}/{word}", headers=headers, timeout=3, allow_redirects=False)
        if response.status_code == 200:
            print(f"[+] Found: {args.url}/{word}")
        elif response.status_code == 403:
            print(f"[!] Forbidden: {args.url}/{word}")
        elif response.status_code == 302:
            print(f"[!] Redirected: {args.url}/{word}")
    except Exception as e:
        print(f"[!] Error occurred while testing {args.url}/{word}: {e}")
        pass

with ThreadPoolExecutor(max_workers=10) as executor:
    try:
        with open(args.wordlist, 'r', errors='ignore') as f:
            wordlist = [line.strip() for line in f.readlines()]
            for word in wordlist:
                executor.submit(fuzz_directory, args, word)
    except FileNotFoundError:
        print(f"[!] Error: Wordlist file '{args.wordlist}' not found.")
        sys.exit(1)