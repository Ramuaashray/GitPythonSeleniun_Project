import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

product_search = "m"
name ="rahulshettyacademy"
expectedList = ["Cucumber - 1 Kg", "Raspberry - 1/4 Kg", "Strawberry - 1/4 Kg"]
ActualList =[]
chromedriver_path = r"C:\Browsers\chromedriver-win64\chromedriver.exe"
service_obj1 =Service(chromedriver_path)
driver = webdriver.Chrome(service=service_obj1)
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, "input[class='search-keyword']").send_keys(product_search)
time.sleep(2)
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(results)
print(count)
assert count > 0

for result in results:
    item_name = result.find_element(By.XPATH, "h4").text
    ActualList.append(item_name)

    if item_name == "Strawberry - 1/4 Kg":
        result.find_element(By.XPATH, ".//div/a[.='+']").click()

    result.find_element(By.XPATH, "div/button").click()
#assert expectedList == ActualList
print(ActualList)

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
CartProductList = []

cartProducts = driver.find_elements(By.XPATH, "//tr/td[2]/p")
for cartProduct in cartProducts:
    CartProductList.append(cartProduct.text)

print(f"Cartproducts list", CartProductList)


# sum validation
prices = driver.find_elements(By.XPATH, "//tr/td[5]/p")
sum1 = 0
for price in prices:
    sum1 = sum1 + int(price.text)
print(sum1)
totalAmount = int(driver.find_element(By.CSS_SELECTOR, "span[class='totAmt']").text)
assert sum1 == totalAmount

driver.find_element(By.CLASS_NAME, "promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, "button[class='promoBtn']").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
time.sleep(2)
discountAmount = float(driver.find_element(By.XPATH, "//span[@class='discountAmt']").text)
assert discountAmount < totalAmount
applycode = driver.find_element(By.CSS_SELECTOR, "span[class='promoInfo']").text
print(applycode)
print(discountAmount)
driver.find_element(By.XPATH, "//div//button[.='Place Order']").click()
driver.find_element(By.XPATH, "//div/select").click()
#select dropdown countries
dropdown = driver.find_elements(By.XPATH, "//select/option")
for drop in dropdown:
    if drop.text == "India":
        drop.click()
        break

driver.find_element(By.CSS_SELECTOR, ".chkAgree").click()
driver.find_element(By.XPATH, "//div/button").click()
successtext = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]").text
print(successtext)

time.sleep(10)
