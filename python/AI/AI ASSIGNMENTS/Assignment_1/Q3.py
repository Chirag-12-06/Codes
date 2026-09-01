# 3 Write a Python program to check the validity of password input by users.Validation:  
# At least 1 letter between [a-z] and 1 letter between [A-Z].  
# At least 1 number between [0-9].  
# At least 1 character from [$#@].  
# Minimum length 6 characters.  
# Maximum length 16 characters.
        

import re

password = input("Enter Your password: ")
if (6 <= len(password) <= 16 and
    re.search(r'[a-z]', password) and
    re.search(r'[A-Z]', password) and
    re.search(r'[0-9]', password) and
    re.search(r'[$#@]', password)):
    print("Your Password is valid")
else:
    print("Your Password is invalid")
