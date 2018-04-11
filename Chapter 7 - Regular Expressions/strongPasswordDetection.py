#! python3
# strongPasswordDetection.py - checks strength of the password using regex

import re, pyperclip

def strong_password_detection(pw):
    if re.search(r'[A-Z]', pw) != None:
        if re.search(r'[a-z]', pw) != None:
            if re.search(r'([0-9])', pw) != None:
                if len(pw) >= 8:
                    return True
    return False

def copy_paste():
    print(strong_password_detection(pyperclip.paste()))

copy_paste()


