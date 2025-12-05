# Import necessary libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the lists to store product names
list1 = []
list2 = []

# Initialize the webdriver (path to your chromedriver.exe)
#driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
chromedriver_path = r"C:\Browsers\chromedriver-win64\chromedriver.exe"
service_obj = Service(chromedriver_path)
driver = webdriver.Chrome(service=service_obj)

# Open the target webpage
driver.get("https://rahulshettyacademy.com/seleniumPractise/")

#Window Maximizing
driver.maximize_window()

# Find the search input field and type the search term using By.CSS_SELECTOR
driver.find_element(By.CSS_SELECTOR, "input.search-keyword").send_keys("g")

# Wait for products to load after search term is entered
time.sleep(4)

# Count the number of product elements displayed
count = len(driver.find_elements(By.XPATH, "//div[@class='products']/div"))

# Assert that 3 products are displayed (based on the search term "ber")
assert count > 3

# Find the product action buttons (the "Add to Cart" buttons) using By.XPATH
buttons = driver.find_elements(By.XPATH, "//div[@class='product-action']/button")

# Loop through each button and click it to add the products to the cart
for button in buttons:
    # Append the product name to the list (located in parent div's h4 tag)
    list1.append(button.find_element(By.XPATH, "parent::div/parent::div/h4").text)

    # Click on the button to add to cart
    button.click()

# Print the list of product names added to the cart
print(list1)

# Click on the cart icon to view the cart using By.CSS_SELECTOR
driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()

# Proceed to checkout by clicking the "PROCEED TO CHECKOUT" button using By.XPATH
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

# Wait until the promo code input field is visible using WebDriverWait and expected_conditions
wait = WebDriverWait(driver, 8)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "promoCode")))

# Get the list of products in the cart and store their names in list2 using By.CSS_SELECTOR
veggies = driver.find_elements(By.CSS_SELECTOR, "p.product-name")
for veg in veggies:
    list2.append(veg.text)

# Print the list of product names in the cart
print(list2)

# Assert that the product names added to the cart match the ones in the list
assert list == list2

# Get the original amount before applying the promo code using By.CSS_SELECTOR
originalAmount = driver.find_element(By.CSS_SELECTOR, ".discountAmt").text

# Enter the promo code in the appropriate field using By.CLASS_NAME
driver.find_element(By.CLASS_NAME, "promoCode").send_keys("rahulshettyacademy")

# Click the "Apply" button to apply the promo code using By.CSS_SELECTOR
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

# Wait until the promo code result is visible using WebDriverWait and expected_conditions
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.promoInfo")))

# Get the discount amount after applying the promo code using By.CSS_SELECTOR
discountAmount = driver.find_element(By.CSS_SELECTOR, ".discountAmt").text

# Assert that the discount amount is less than the original amount
assert float(discountAmount) < int(originalAmount)

# Print the promo information message (e.g., success message) using By.CSS_SELECTOR
print(driver.find_element(By.CSS_SELECTOR, "span.promoInfo").text)

# Get the amounts of the items in the cart using By.XPATH
amounts = driver.find_elements(By.XPATH, "//tr/td[5]/p")

# Initialize a variable to store the sum of the product prices
sum = 0

# Loop through each amount element and add its value to the sum
for amount in amounts:
    sum = sum + int(amount.text)  # Adding each product's price

# Print the sum of the product amounts in the cart
print(sum)

# Get the total amount after discount using By.CLASS_NAME
totalAmount = int(driver.find_element(By.CLASS_NAME, "totAmt").text)

# Assert that the sum of the product prices equals the total amount
assert sum == totalAmount

# Close the driver (browser)
driver.quit()
