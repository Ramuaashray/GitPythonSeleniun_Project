from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.shop import shopPage


class BrowserUtils:
    pass


class ShopPage:
    pass


class LoginPage(BrowserUtils):
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "username")
        self.password = (By.ID, "password")
        self.sign_button = (By.CSS_SELECTOR, "#signInBtn")


    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.sign_button).click()
        #wait = WebDriverWait(driver, 10)
        # wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
        # print(driver.find_element(By.CSS_SELECTOR, ".alert-danger").text)
        shop_page = shopPage(self.driver, self.countryName)
        return shop_page