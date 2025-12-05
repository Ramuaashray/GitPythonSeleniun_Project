from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_e2e(browserinstance):
    driver = browserinstance
    wait = WebDriverWait(driver, 10)

    driver.implicitly_wait(4)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    print(driver.current_url)
    print(driver.title)

    driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
    products = driver.find_elements(By.XPATH, "//div[@class= 'card h-100']")

    # List of products to add to cart
    products_to_add = ["iphone X", "Samsung Note 8"]  # Add the second product here
    added_products = []  # To store successfully added products

    for product in products:
        productName = product.find_element(By.XPATH, ".//h4/a").text  # Use relative XPath
        if productName in products_to_add:  # Check if the product is in our list
            product.find_element(By.XPATH, ".//div/button").click()  # Use relative XPath
            added_products.append(productName)  # Store the added product
            products_to_add.remove(productName)  # Remove from list to avoid duplicate clicks

        if not products_to_add:  # Exit loop if all products are added
            break

    # Print products added to cart
    print(f"Products added to cart: {added_products}")

    # Proceed with checkout process
    driver.find_element(By.CSS_SELECTOR, "a[class='nav-link btn btn-primary']").click()

    # Locate only product rows that contain the "Remove" button
    cart_product_rows = driver.find_elements(By.XPATH,
                                             "//table[@class='table table-hover']//tbody/tr[td/button[contains(., 'Remove')]]")

    # Get the correct product count
    cart_product_count = len(cart_product_rows)

    # Print correct product count
    print(f"✅ Number of products in checkout: {cart_product_count}")

    driver.find_element(By.XPATH, "//button[@class = 'btn btn-success']").click()
    driver.find_element(By.ID, "country").send_keys("ind")
    wait = WebDriverWait(driver, 10)
    wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
    driver.find_element(By.LINK_TEXT, "India").click()
    driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
    driver.find_element(By.XPATH, "//input[@class='btn btn-success btn-lg']").click()
    # Assertion for success message
    successmsg = driver.find_element(By.CSS_SELECTOR, "div[class='alert alert-success alert-dismissible']").text
    assert "Success! Thank you!" in successmsg
    print(successmsg)

    # Verify checkout contains the expected number of products
    assert cart_product_count == len(added_products), "❌ Mismatch in product count in cart!"
    print("✅  Test Passed: Product count matches!")
    print("\u2705 Test Passed: Product count matches!")  # ✅
    print("\u274C Test Failed: Product count mismatch!")  # ❌
    print("\U0001F525 Performance is great!")  # 🔥

    # Close the alert and browser
    driver.find_element(By.CSS_SELECTOR, "a[class='close']").click()
    driver.close()
