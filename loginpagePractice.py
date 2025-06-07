from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.implicitly_wait(5)
driver.find_element(By.ID, "username").send_keys("rahulshettyacademy")
driver.find_element(By.NAME,"password").send_keys("learning")
driver.find_element(By.ID,"signInBtn").click()

elements = driver.find_elements(By.XPATH,"//div[class='card h-100']")

for product in elements:

    product_name = product.find_element(By.XPATH, "div/h4/a").text
    if product_name == "Blackberry":
        product.find_element(By.XPATH, "//div/button").click()


driver.find_element(By.CSS_SELECTOR, "a[class='nav-link btn btn-primary']").click()
driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()

#handle the auto sugsstive dropdown
driver.find_element(By.ID,'country').send_keys("Ind")
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(By.LINK_TEXT, "India").click()
