from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.implicitly_wait(5)
#driver.find_element(By.LINK_TEXT, "https://rahulshettyacademy.com/angularpractice/shop").click()

# or using regualr expression(do it is using xpath or css is feasible option)
#xpath syntax: //tagname[@attribute='value']
# css syntax: tagename[attribute='value']
driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
#perform chaining of the elements when we have multiple elements with same name
for element in products:
    productName = element.find_element(By.XPATH, "div/h4/a").text
    if productName == "Blackberry":
        element.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "a[class='nav-link btn btn-primary']").click()
driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-success']").click()

#synatx to verify the xpath or css in console winodw
#xpath
#$x("button[class='btn btn-success']")
#css (remove the dollar for the css
#$("button[class='btn btn-success']")

#handle the auto sugsstive dropdown
driver.find_element(By.ID,'country').send_keys("Ind")
#applying the explict wait to invidudal elements
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(By.LINK_TEXT, "India").click()
driver.close()
