from selenium.common import NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageObjectModelKeyConcepts.PomPoorna.shoppage import ShopPage
from PageObjectModelKeyConcepts.pythonSel.conftest import browserInstance
from PageObjectModelKeyConcepts.utils.browserutils import BrowserUtils


# from utils

class LoginPage(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.username_input = (By.ID, "username")
        self.password_input = (By.NAME, "password")
        self.signin_button = (By.ID, "signInBtn")

    def login(self,username, password):
        #purpose of * is to convert the varaible into 2 arguments
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.signin_button).click()



    def handle_unexpected_alert(self):
        try:
            # Wait for a short time to see if an alert appears
            WebDriverWait(self.driver, 10).until(EC.alert_is_present())

            # Get the alert
            alert = self.driver.switch_to.alert

            # Get alert text (for logging/debugging)
            alert_text = alert.text
            print(f"Alert detected: {alert_text}")

            # Accept the alert (click OK)
            alert.accept()

            # Or to dismiss (click Cancel) use:
            # alert.dismiss()

            return True
        except NoAlertPresentException:
            return False


        except Exception as e:
            print(f"Error handling alert: {e}")
            return False
