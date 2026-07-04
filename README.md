# QuickFuzz

A lightweight, multithreaded HTTP directory fuzzer written in Python. This tool helps security researchers and penetration testers discover hidden directories and files on web servers by brute-forcing URLs with a custom wordlist.

## Features

* **Fast & Concurrent:** Utilizes `ThreadPoolExecutor` (10 workers) for rapid multithreaded fuzzing.
* **Status Code Handling:** Specifically identifies and highlights `200 OK`, `403 Forbidden`, and `302 Redirect` responses.
* **Graceful Exit:** Safely handles `Ctrl+C` (SIGINT) to stop the scanning process immediately without terminal clutter.
* **Pre-flight Check:** Verifies that the base URL is reachable before starting the intensive fuzzing process.
* **Custom User-Agent:** Spoofs a standard browser User-Agent to bypass basic scraping blocks.

## Prerequisites

* Python 3.x
* `requests` library

## Installation

1. Clone the repository:
   ```bash

   git clone [https://github.com/VISION-SAM/pyDirFuzzer.git](https://github.com/VISION-SAM/pyDirFuzzer.git)
   
   cd QuickFuzz


# Install the required dependencies: 

    pip install requests


# Usage

Run the script from the command line by providing a base URL and a wordlist.
    Bashpython fuzzer.py -u <TARGET_URL> -w <PATH_TO_WORDLIST>

Arguments   ArgumentShort   DescriptionRequired
--url           -u          The base URL to fuzz (e.g., http://example.com)Yes
--wordlist      -w          Path to the text file containing the wordlist


## Example
    
    python QuickFuzz.py -u [http://10.10.10.10](http://10.10.10.10) -w /usr/share/wordlists/dirb/common.txt


## Sample Output:
    Plaintext[+] Found: [http://10.10.10.10/admin](http://10.10.10.10/admin)
    [!] Forbidden: [http://10.10.10.10/server-status](http://10.10.10.10/server-status)
    [!] Redirected: [http://10.10.10.10/login](http://10.10.10.10/login)


⚠️ DisclaimerThis tool is designed for educational purposes and authorized security testing only. Do not use this tool against any web application or server that you do not own or do not have explicit permission to test. The author is not responsible for any misuse or damage caused by this program.
