from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chromedriver_path = r"C:\Browsers\chromedriver-win64\chromedriver.exe"
service_obj1 =Service(chromedriver_path)
driver = webdriver.Chrome(service=service_obj1)

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)

#2nd driver invoke without services
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com")
driver.maximize_window()
print(driver.title)
print(driver.current_url)