import time
from selenium import webdriver

options = webdriver.ChromeOptions()
time.sleep(4)

driver = webdriver.Chrome(options=options)
driver.get('https://dzen.ru')
time.sleep(10)

