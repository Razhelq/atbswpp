import os, shutil
from selenium import webdriver
import sys


# driver.implicitly_wai

if os.path.isdir('flickr') == True:
    shutil.rmtree('flickr')
else:
    os.makedirs('flickr', exist_ok=True)

url = 'https://www.flickr.com/search/?text='

