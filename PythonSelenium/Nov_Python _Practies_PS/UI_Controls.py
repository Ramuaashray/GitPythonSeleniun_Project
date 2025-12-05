import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from typing_extensions import assert_type

chromedriver_path = r"C:\Browsers\chromedriver-win64\chromedriver.exe"
service_obj1 =Service(chromedriver_path)
driver = webdriver.Chrome(service=service_obj1)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()
        break

Radiobuttons = driver.find_elements(By.CSS_SELECTOR, "input[type='radio']")
print(len(Radiobuttons))

for Radiobutton in Radiobuttons:
    if Radiobutton.get_attribute("value") == "radio2":
        Radiobutton.click()
        assert Radiobutton.is_selected()
        break


assert driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.ID, "hide-textbox").click()
assert not driver.find_element(By.ID, "displayed-text").is_displayed()