from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#driver = webdriver.Chrome(executable_path="C:\Browsers\chromedriver-win64\chromedriver.exe")
chromedriver_path = r"C:\Browsers\chromedriver-win64\chromedriver.exe"
# Create a Service object for ChromeDriver
service_obj = Service(chromedriver_path)
# Set up the WebDriver using the service object
driver = webdriver.Chrome(service=service_obj)

driver.get("https://login.salesforce.com/")
driver.find_element(By.CSS_SELECTOR, "#username").send_keys("Rahul")
driver.find_element(By.CSS_SELECTOR, ".password").send_keys("shetty")
driver.find_element(By.CSS_SELECTOR, ".password").clear()
driver.find_element(By.LINK_TEXT, "Forgot Your Password?").click()
driver.find_element(By.XPATH, "//input[@name='cancel']").click()
print(driver.find_element(By.XPATH, "//form[@name='login']/div[1]/label").text)
print(driver.find_element(By.CSS_SELECTOR, "form[name='login'] label:nth-child(3)").text)