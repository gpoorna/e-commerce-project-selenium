from selenium.common import NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageObjectModelKeyConcepts.PomPoorna.checkoutconfirmation import CheckoutConfirmation


class ShopPage:
    def __init__(self,driver):
        self.driver = driver
        self.products = (By.XPATH, "//div[@class='card h-100']")
        self.checkout_button = (By.CSS_SELECTOR, "a[class*='btn-primary']")



    def add_product_to_cart(self, product_name):

        self.products = self.driver.find_elements(*self.products)

        # perform chaining of the elements when we have multiple elements with same name
        for element in self.products:
            product = element.find_element(By.XPATH, "div/h4/a").text
            if product == product_name:
                element.find_element(By.XPATH, "div/button").click()

    def goToCart(self):

        self.checkout_button = self.driver.find_element(*self.checkout_button).click()
        checkout_confirmation = CheckoutConfirmation(self.driver)
        return checkout_confirmation

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


