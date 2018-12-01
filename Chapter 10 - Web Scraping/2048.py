from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox(executable_path=r'geckodriver.exe')
browser.get('https://gabrielecirulli.github.io/2048/')
body = browser.find_element_by_tag_name('body')
count = 0
while count < 10000:
    body.send_keys(Keys.UP)
    body.send_keys(Keys.RIGHT)
    body.send_keys(Keys.DOWN)
    body.send_keys(Keys.LEFT)
    count += 1