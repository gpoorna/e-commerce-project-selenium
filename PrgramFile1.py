import time

from selenium import webdriver

driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://www.hotstar.com/in/home")
time.sleep(20)