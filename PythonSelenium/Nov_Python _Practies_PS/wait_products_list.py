import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

name ="rahulshettyacademy"
chromedriver_path = r"C:\Browsers\chromedriver-win64\chromedriver.exe"
service_obj1 =Service(chromedriver_path)
driver = webdriver.Chrome(service=service_obj1)
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, "input[class='search-keyword']").send_keys("ber")
time.sleep(2)
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(results)
print(count)
assert count > 0

for result in results:
    result.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
#driver.find_element(By.CSS_SELECTOR, "input[placeholder='Enter promo code']").send_keys("rahulshettyacademy")
#driver.find_element(By.CLASS_NAME, "promoCode").send_keys("rahulshettyacademy")
#time.sleep(2)
driver.find_element(By.CLASS_NAME, "promoCode").send_keys("rahulshettyacademy")

driver.find_element(By.CSS_SELECTOR, "button[class='promoBtn']").click()
#time.sleep(5)
applycode =driver.find_element(By.CSS_SELECTOR, "span[class='promoInfo']").text
print(applycode)

time.sleep(10)
