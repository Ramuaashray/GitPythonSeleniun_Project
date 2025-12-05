from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chromedriver_path = r"C:\Browsers\chromedriver-win64\chromedriver.exe"
service_obj1 =Service(chromedriver_path)
driver = webdriver.Chrome(service=service_obj1)
driver.implicitly_wait(5)
browsersortedlist = []

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
# click on header column
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()

#collect all vegies names -> browser sorted list
VeggiesWebElement = driver.find_elements(By.XPATH, "//tr/td[1]")
for element in VeggiesWebElement:
    browsersortedlist.append(element.text)
#sort this browser sorted veggies list
originalVeggiesList = browsersortedlist.copy()
browsersortedlist.sort()
#assertion
print(originalVeggiesList)
print(browsersortedlist)