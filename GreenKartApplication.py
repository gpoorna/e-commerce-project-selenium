from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.XPATH, "//input[@type='search']").send_keys("ber")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
products = driver.find_elements(By.XPATH, "//div[@class='products']/div")
for product in products:
    driver.find_element(By.XPATH,"//div[@class='product-action']/button").click()

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CLASS_NAME, "promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.LINK_TEXT, "Apply").click()

wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
#print(driver.find_element(By.CLASS_NAME,"promoInfo").text)
driver.find_element(By.LINK_TEXT,"Place Order").click()