# 🗝️ Python Web Login Brute-Forcer

## 📖 Overview
This is a custom-built Python script designed to automate dictionary attacks against web login portals. It demonstrates how to interact with web application authentication mechanisms by sending automated HTTP POST requests containing username and password payloads.



### 🧠 The "Smart" Logic
Instead of relying on HTTP Status Codes (like `200 OK`), which are often misleading during web authentication, this tool intelligently parses the raw HTML response. It looks for **Positive Success Indicators** (like the appearance of a "logout" or "welcome" message) to accurately determine when a payload has successfully bypassed the login screen.

## ✨ Features
* **Automated POST Requests:** Rapidly packages and delivers credentials to a target HTML form.
* **Custom Wordlists:** Imports external `.txt` files containing common or leaked passwords.
* **Smart Verification:** Bypasses "False Negatives" by searching the Document Object Model (DOM) for successful login indicators rather than generic failure messages.
* **Fast Execution:** Instantly halts the loop (`break`) the moment the correct password is found.

## 🛠️ Requirements
* Python 3.x
* The `requests` library

To install the required library, run:
`pip install requests`

## 🚀 Usage

1. Clone or download this repository to your local machine.
2. Create a password dictionary named `passwords.txt` and place it in the same directory as the script.
3. Open `brute.py` and modify the following variables to match your authorized target:
   * `target_url`: The backend script processing the login (e.g., `http://target.com/login.php`)
   * `target_username`: The account username you are auditing.
   * `login_data`: Ensure the payload dictionary keys match the actual HTML form's `name` attributes (e.g., `uname` and `pass`).
4. Run the script:
`python brute.py`

---

## ⚠️ Legal Disclaimer
> **FOR EDUCATIONAL AND AUTHORIZED TESTING PURPOSES ONLY.**
> 
> This tool was developed to help cybersecurity students and professionals understand credential stuffing, dictionary attacks, and authentication vulnerabilities. 
>
> **DO NOT** use this script against any system, network, or application without explicit, documented permission. The developer assumes no liability and is not responsible for any misuse, damage, or legal consequences caused by the use of this tool.
