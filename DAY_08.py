"""
 Challenge: Password Strength Checker & Suggestion Tool

Build a Python script that checks the strength of a password based on:
1. Length (at least 8 characters)
2. At least one uppercase letter
3. At least one lowercase letter
4. At least one digit
5. At least one special character (e.g., @, #, $, etc.)

Your program should:
- Ask the user to input a password.
- Tell them what's missing if it's weak.
- If the password is strong, confirm it.
- Suggest a strong random password if the input is weak.

Bonus:
- Hide password input using `getpass` (no echo on screen).
"""

import string
import random
import getpass

def check_Password_strength(password):
    issue = []
    if len(password) < 8:
        issue.append("Too Short (minimum 8 characters)")
        #.islower is a checker method which just check weather this value is lower or not     
    if not any(c.islower() for c in password):
        issue.append("Missing lower case letter")
    if not any(c.isupper() for c in password):
        issue.append("Missing upper case letter")
    if not any(c.isdigit() for c in password):
        issue.append("Missing digit")
    if not any(c in string.punctuation for c in password):
        issue.append("Missing a spacial character")
    return issue

def generate_strong_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation

    # assignment:- def generate_strong_password(length=26): chars = string.ascii_lowercase + string.digits + string.punctuation
    
    return "".join(random.choice(chars) for _ in range(length))
        
password = getpass.getpass("Enter a Password: ")
issue = check_Password_strength(password)

if not issue:
    print("Strong password! You are good to go")
else:
    print("You get weak password")
    for issues in issue:
        print(f"- {issue}")
        
suggestion = generate_strong_password()
print("\n suggesting you a strong password")
print(suggestion)
