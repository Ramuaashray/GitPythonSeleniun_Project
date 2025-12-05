import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


chromedriver_path = r"C:\Browsers\chromedriver-win64\chromedriver.exe"

# Create a Service object for ChromeDriver
service_obj = Service(chromedriver_path)

# Set up the WebDriver using the service object
driver = webdriver.Chrome(service=service_obj)


#driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
driver.find_element(By.NAME,"email").send_keys("Hell@gamil.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("1234")
driver.find_element(By.ID,"exampleCheck1").click()
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Ramu")
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()
driver.find_element(By.XPATH,"//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
assert "Success" in message

driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("helloagain")


