import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class file_validation():
    def __init__(self, driver):
        self.driver = driver
        self.toast_Locator =(By.CSS_SELECTOR, ".Toastify__toast-body div:nth-child(2)")
        self.price_column =(By.XPATH, "//div[text()='Price']")


        global fruit_name
        global newValue
        fruit_name = "Apple"
        newValue = "15"

    def file_validation(self):
        wait = WebDriverWait(self.driver, 5)
        toast_locator = (self.toast_Locator)
        wait.until(expected_conditions.visibility_of_element_located(toast_locator))
        print(self.driver.find_element(*toast_locator).text)
        priceColumn = self.driver.find_element(*self.price_column).get_attribute("data-column-id")
        actual_price = self.driver.find_element(By.XPATH, "//div[text()='" + fruit_name + "']/parent::div/parent::div/div[@id='cell-" + priceColumn + "-undefined']").text
        assert actual_price == newValue

