from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

chromedriver_path = r"C:\Browsers\chromedriver-win64\chromedriver.exe"
service_obj1 =Service(chromedriver_path)
driver = webdriver.Chrome(service=service_obj1)

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
# Xpath- //tagname[@attribute='value']
# CCs selector - tagname[attribute='value']

#driver.find_element(By.NAME, "name").send_keys("Ramu_Selenium")
driver.find_element(By.XPATH, "(//input[@name='name'])[1]").send_keys("ramu-selenium")
driver.find_element(By.NAME, "email").send_keys("Hello@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID, "exampleCheck1").click()
driver.find_element(By.CSS_SELECTOR, "input[value='option1'").click()
driver.find_element(By.XPATH, "(//input[@name='name'])[1]").send_keys("selenium")

driver.find_element(By.XPATH, "(//input[@class='form-control'])[2]").click()
#static dropdowns
dropdown =Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")

driver.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-dismissible").text
print(message)
assert "Success" in message