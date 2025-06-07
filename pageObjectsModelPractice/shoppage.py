from selenium.webdriver.common.by import By


class ShopPage:
    def __int__(self, driver):
        self.driver = driver
        self.products = (By.XPATH, "//div[@class='card h-100']")
        self.checkout_button = (By.CSS_SELECTOR, "a[class='nav-link btn btn-primary']")

    def add_product_to_cart(self, product_name):

        self.products = self.driver.find_elements(*self.products)

        # perform chaining of the elements when we have multiple elements with same name
        for element in self.products:
            product = element.find_element(By.XPATH, "div/h4/a").text
            if product == product_name:
                element.find_element(By.XPATH, "div/button").click()

    def goToCart(self):

        self.checkout_button = self.driver.find_elemen(*self.checkout_button).click()

