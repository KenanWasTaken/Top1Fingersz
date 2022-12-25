from selenium import webdriver
import time
from selenium.webdriver.common.by import By

browser = webdriver.Edge("msedgedriver.exe")
browser.get("https://10fastfingers.com/typing-test/english")

time.sleep(8)

while True:
    try:
        word = browser.find_element(By.CLASS_NAME, 'highlight')
        print(word.text)
        textinput = browser.find_element(By.ID, "inputfield")
        textinput.send_keys(word.text + " ")
    except:
        pass