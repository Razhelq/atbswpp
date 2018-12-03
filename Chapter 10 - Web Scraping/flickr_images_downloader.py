import os, shutil, requests, bs4
from selenium import webdriver
import time
import sys


if os.path.isdir('flickr') == True:
    shutil.rmtree('flickr')
else:
    os.makedirs('flickr', exist_ok=True)

url = 'https://www.flickr.com/search/?text=something'

browser = webdriver.Firefox(executable_path=r'geckodriver.exe')
browser.get(url)
browser.implicitly_wait(2)
pics = browser.find_elements_by_class_name('overlay')
for i in range(20):
    browserr = webdriver.Firefox(executable_path=r'geckodriver.exe')
    browserr.get(url)
    browserr.implicitly_wait(2)
    pics = browserr.find_elements_by_class_name('overlay')
    browserr.get(pics[i].get_attribute('href'))
    browserr.implicitly_wait(2)
    pic = browserr.find_element_by_class_name('toggle-icon')
    browserr.implicitly_wait(2)
    pic.click()
    browserr.implicitly_wait(2)
    pic = browserr.find_element_by_class_name('is-real-fullscreen')
    browserr.implicitly_wait(2)
    pic.click()
    try:
        pic_elem = browserr.find_element_by_class_name('zoom-large')
        pic_src = pic_elem.get_attribute('src')
    except:
        try:
            pic_elem = browserr.find_element_by_class_name('main-photo')
            pic_src = pic_elem.get_attribute('src')
        except:
            pass
    try:
        res = requests.get(pic_src)
    except:
        pass
    browserr.close()

    try:
        image_file = open(os.path.join('flickr', os.path.basename(pic_src)), 'wb')
        for chunk in res.iter_content(100000):
            image_file.write(chunk)
        image_file.close()
    except:
        pass

browser.close()