import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

chromedriver_path = r"C:\Browsers\chromedriver-win64\chromedriver.exe"
service_obj1 =Service(chromedriver_path)
driver = webdriver.Chrome(service=service_obj1)

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()

driver.find_element(By.ID, "autosuggest").send_keys("Ind")
time.sleep(2)

Countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
print(len(Countries))

for country in Countries:
    if country.text == "India":
        country.click()
        break
#time.sleep(2)
#print(driver.find_element(By.ID, "autosuggest").text)
text = (driver.find_element(By.ID, "autosuggest").get_attribute("value"))
print(text)
assert text == "India"
