from selenium import webdriver
import sys
import time

url = 'https://poczta.domena.pl/'
if sys.argv[1] != None and sys.argv[2] != None and sys.argv[3] != None:
    # login to the mailbox
    browser = webdriver.Firefox(executable_path=r'geckodriver.exe')
    browser.get(url)
    login_elem = browser.find_element_by_id('rcmloginuser')
    password_elem = browser.find_element_by_id('rcmloginpwd')
    login_elem.send_keys('')
    password_elem.send_keys('')
    password_elem.submit()

    # open new email card
    time.sleep(1)
    browser.current_url
    new_mail_elem = browser.find_element_by_id('rcmbtn109')
    new_mail_elem.click()

    # fill the email and send
    time.sleep(1)
    browser.current_url
    recipient_elem = browser.find_element_by_id('_to')
    subject_elem = browser.find_element_by_id('compose-subject')
    content_elem = browser.find_element_by_id('composebody')
    send_elem = browser.find_element_by_id('rcmbtn107')
    recipient = sys.argv[1]
    subject = sys.argv[2]
    content = sys.argv[3]
    recipient_elem.send_keys(recipient)
    subject_elem.send_keys(subject)
    content_elem.send_keys(content)
    send_elem.click()