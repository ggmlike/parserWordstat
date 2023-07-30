import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec


def time_sleep_random():
    time_sleep_load_page = random.randint(3, 17)
    time.sleep(time_sleep_load_page)


options = webdriver.ChromeOptions()
time_sleep_random()
driver = webdriver.Chrome(options=options)
driver.get('https://wordstat.yandex.ru/')
wait = WebDriverWait(driver, 10)
elem_vision = wait.until(Ec.visibility_of_element_located((By.CSS_SELECTOR, "input.b-search__type")))
elemen = driver.find_element(By.CLASS_NAME, "b-search__type.b-search__type_with-regions_yes")
elemen.click()
time.sleep(50)
