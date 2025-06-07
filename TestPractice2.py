from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import actions
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
name = "Ravi"
driver.maximize_window()
driver.implicitly_wait(10)
#find_elements used when we have multiple elements with same name
'''radioButtons1 = driver.find_elements(By.CLASS_NAME, "radioButton")
#click() elements are used when to permform click operation
radioButtons1[2].click()
#assert performs avlidation check wheather the condition is true or not
#is_selected used to verify wheather elemets are selected or not
assert radioButtons1[2].is_selected()

driver.find_element(By.ID, "autocomplete").send_keys("ind")
#find elemets retruns multiple elements and store in the list
#css selector plays an important role in fetching the elememts
#css selector syantax: tagname[attribute='value'] tagname
countries = driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item'] div")
print(len(countries))

for country in countries:
    if country.text == "India":
        country.click()

        break
dropdown = Select(driver.find_element(By.ID, "dropdown-class-example"))
dropdown.select_by_index(1)
driver.implicitly_wait(5)
driver.find_element(By.ID, "checkBoxOption1").click()'''

''' Note: window_handles functions return the windows name and stores in the form of list using which we can easily perform the switch operation '''
'''
#switching from one window to another window
current_window = driver.current_window_handle
print("first window title:" +driver.title)
driver.find_element(By.ID, "openwindow").click()
#perform the switch operation using window_handles method
driver.switch_to.window(driver.window_handles[1])
print("second winodw title:" +driver.title)
#swictching back to curren t window
driver.switch_to.window(current_window) '''

#swiching from one to tab to another tab
'''driver.find_element(By.LINK_TEXT,"Open Tab").click()
windowsOpened = driver.window_handles
driver.switch_to.window(windowsOpened[1])
#Navigates to next window use window_Handles to get name
driver.find_element(By.LINK_TEXT, "Access all our Courses").click()
driver.close()
driver.switch_to.window(windowsOpened[0])'''

#handling the javascript
'''driver.find_element(By.ID, "name").send_keys(name)
#switch to alert
#driver.find_element(By.ID, "alertbtn").click()
driver.find_element(By.ID, "confirmbtn").click()
alert = driver.switch_to.alert
alertTextInfo = alert.text
print(alertTextInfo)
assert name in alertTextInfo
#to accepts the alert
#alert.accept()
alert.dismiss()'''

#mouse hover action
#Note:ActionChains is used to perform any new Actions
#move_to_element is used to perform the mouse hover operation
actions = ActionChains(driver)
actions.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
#to perform the right click of an elememnt
actions.context_click(driver.find_element(By.LINK_TEXT, "Top")).click().perform()

#Handle the frames
















