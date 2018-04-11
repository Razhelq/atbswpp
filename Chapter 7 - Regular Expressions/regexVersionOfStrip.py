#! python3
# regexVersionOfStrip.py - strip like regex version app

import re, pyperclip

def strip_reg(text, letter=''):
    # If there is no 2nd argument fuction removes spaces from the beginning and the and of the string
    if letter == '':
        return re.search(r'(\S.*\S)', text, re.DOTALL).group()
    # If the is 2nd argument function will remove it from the string
    return re.compile(r'{}'.format(letter)).sub('', text)

def copy_paste():
    print(strip_reg(pyperclip.paste(), ''))

copy_paste()