from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chromedriver_path = r"C:\Browsers\chromedriver-win64\chromedriver.exe"
service_obj1 =Service(chromedriver_path)
driver = webdriver.Chrome(service=service_obj1)

driver.get("https://rahulshettyacademy.com/client/#/auth/login")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, "a[class='btn1']").click()
driver.find_element(By.CSS_SELECTOR, "input[placeholder='First Name']").send_keys("Raju")
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Last Name']").send_keys("K")
driver.find_element(By.XPATH, "//input[@class='ng-touched']").send_keys("rajuk@gmial.com")
driver.find_element(By.CSS_SELECTOR, "#userEmail").send_keys("123456789")
driver.find_element(By.CSS_SELECTOR, "select[formcontrolname='occupation']").click()
driver.find_element(By.CSS_SELECTOR, "option[value='2: Student']").click()
driver.find_element(By.CSS_SELECTOR, "input[value='Male']").click()
