from selenium.webdriver.common.by import By


class LoginPage:
    def __int__(self,driver):
        self.driver = driver
        self.username_input = (By.ID, "username")
        self.password_input = (By.NAME, "password")
        self.signin_button = (By.ID, "signInBtn")

    def login(self):
        #purpose of * is to convert the varaible into 2 arguments
        self.driver.find_element(*self.username_input).send_keys("rahulshettyacademy")
        self.driver.find_element(*self.password_input).send_keys("learning")
        self.driver.find_element(*self.signin_button).click()
