import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chromedriver_path = r"C:\Browsers\chromedriver-win64\chromedriver.exe"
service_obj1 =Service(chromedriver_path)
driver = webdriver.Chrome(service=service_obj1)
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()

ProductNames = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

for product in ProductNames:
    Productname = product.find_element(By.XPATH, "div/h4").text
    if Productname == "Blackberry":
        product.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
driver.find_element(By.CSS_SELECTOR, "button[class*='btn btn-success']").click()
driver.find_element(By.ID, "country").send_keys("India")
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "div[class='suggestions'] ul li a")))
driver.find_element(By.XPATH, "//a[text()='India']").click()

driver.find_element(By.CSS_SELECTOR, "label[for='checkbox2']").click()
driver.find_element(By.CSS_SELECTOR, "input[value='Purchase']").click()

SuccessText = driver.find_element(By.CSS_SELECTOR, "div[class*='alert-dismissible']").text
print(SuccessText)