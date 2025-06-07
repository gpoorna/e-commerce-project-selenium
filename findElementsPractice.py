import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait
from selenium.webdriver.support.select import Select

driver =webdriver.Chrome()
driver.get("https://www.aznude.com/browse/videos/popular/days/1.html")
driver.implicitly_wait(10)
driver.maximize_window()

#find the elements by image tag
element = driver.find_element(By.ID, "query").send_keys("kate winslet")
#element = driver.find_element(By.XPATH, "//input[@type='submit']").click()

#select class provide the methods to handle the options in dropdown







