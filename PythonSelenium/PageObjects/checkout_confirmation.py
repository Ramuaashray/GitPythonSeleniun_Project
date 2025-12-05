from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

global countryName
class Checkout_Confirmation:


    def __init__(self,driver, countryName: str):
        self.driver = driver
        self.countryName = countryName
        self.checkout_button = (By.CSS_SELECTOR, "button[class*='btn btn-success']")
        self.country_input = (By.ID, "country")
        self.country_option = (By.LINK_TEXT, self.countryName)
        self.checkbox = (By.CSS_SELECTOR, "label[for='checkbox2']")
        self.submit_button = (By.CSS_SELECTOR, "input[value='Purchase']")
        self.success_message = (By.CSS_SELECTOR, "div[class*='alert-dismissible']")





    def checkout(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(*self.checkout_button).click()

    def enter_delivery_address(self, countryName):
        self.driver.find_element(*self.country_input ).send_keys(countryName)
        wait = WebDriverWait(self.driver, 10)
        #wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "div[class='suggestions'] ul li a")))
        wait.until(expected_conditions.visibility_of_element_located(self.country_option))
        self.driver.find_element(*self.country_option).click()

        self.driver.find_element(*self.checkbox).click()
        self.driver.find_element(*self.submit_button).click()

    def validate_order(self):
        SuccessText = self.driver.find_element(*self.success_message).text
        assert "Success! Thank you!" in SuccessText
        print(SuccessText)




