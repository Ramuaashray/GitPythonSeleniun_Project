

from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait

# Initialize the webdriver (path to your chromedriver.exe)
#driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
chromedriver_path = r"C:\Browsers\chromedriver-win64\chromedriver.exe"
service_obj = Service(chromedriver_path)
driver = webdriver.Chrome(service=service_obj)

# Open the target webpage
driver.get("https://rahulshettyacademy.com/seleniumPractise/")

#Window Maximizing
driver.maximize_window()

''''# Initialize the webdriver
chromedriver_path = r"C:\Browsers\chromedriver-win64\chromedriver.exe"
service_obj = Service(chromedriver_path)
driver = webdriver.Chrome(service=service_obj)

# Open the target webpage and maximize the window
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()'''

# Function to add items to the cart
def add_items_to_cart(item_names):
    for item in item_names:
        try:
            item_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, f"//h4[contains(text(), '{item}')]/following-sibling::div/button"))
            )
            item_button.click()
            print(f"Added {item} to cart.")
        except Exception as e:
            print(f"Error adding {item}: {e}")

# Add Vegetables and Fruits to Cart
vegetable_list = ["Tomato", "Onion", "Carrot", "Brinjal", "Potato"]
fruit_list = ["Apple", "Banana", "Mango"]

add_items_to_cart(vegetable_list)
add_items_to_cart(fruit_list)

# Wait for the cart to update
time.sleep(2)

# Wait for the cart button to be clickable and navigate to the cart
'''cart_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '#/cart')]")))
cart_button.click()'''
driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
time.sleep(2)

# Verify Vegetables in Cart
for vegetable in vegetable_list:
    try:
        driver.find_element(By.XPATH, f"//div[@class='cartItem'][contains(text(), '{vegetable}')]")
        print(f"{vegetable} found in cart.")
    except:
        print(f"{vegetable} not found in cart!")

# Verify Fruits in Cart
for fruit in fruit_list:
    try:
        driver.find_element(By.XPATH, f"//div[@class='cartItem'][contains(text(), '{fruit}')]")
        print(f"{fruit} found in cart.")
    except:
        print(f"{fruit} not found in cart!")

# Capture original price
try:
    original_price_element = driver.find_element(By.XPATH, "//span[@class='totAmt']")
    original_price = float(original_price_element.text.replace('₹', '').strip())
    print(f"Original Price: ₹{original_price}")
except Exception as e:
    print("Error extracting original price:", e)

# Proceed to Checkout
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
time.sleep(2)

# Apply Discount Code (if applicable)
discount_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Enter promo code']"))
)
discount_input.send_keys("DISCOUNT2025")  # Replace with a valid code if available
discount_input.send_keys(Keys.RETURN)
time.sleep(2)

# Verify Discounted Price
try:
    discounted_price_element = driver.find_element(By.XPATH, "//span[@class='totAmt']")
    discounted_price = float(discounted_price_element.text.replace('₹', '').strip())
    print(f"Discounted Price: ₹{discounted_price}")

    assert discounted_price < original_price, "Discount was not applied correctly!"
except Exception as e:
    print(f"Error applying discount: {e}")

# Close the browser
driver.quit()
