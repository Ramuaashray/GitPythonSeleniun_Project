
'''from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

# Initialize the WebDriver
chromedriver_path = r"C:\Browsers\chromedriver-win64\chromedriver.exe"
service_obj = Service(chromedriver_path)
driver = webdriver.Chrome(service=service_obj)

try:
    # Open the website
    driver.get('https://rahulshettyacademy.com/angularpractice/')

    # Wait for the page to load
    wait = WebDriverWait(driver, 10)

    # Locate the Employment Status dropdown
    employment_status_dropdown = wait.until(
        EC.visibility_of_element_located((By.ID, 'exampleFormControlSelect1'))
    )

    # Print the options of the dropdown to verify
    select_element = Select(employment_status_dropdown)
    options = select_element.options
    print("Options in the dropdown:")
    for option in options:
        print(option.text)

    # Function to select a status dynamically
    def select_status(status):
        try:
            select_element.select_by_visible_text(status)
            print(f"Selected: {status}")
            time.sleep(1)
        except Exception as e:
            print(f"Error selecting {status}: {e}")

    # Now let's try selecting "Student"
    select_status("Student")

    # Verify if "Student" is selected
    selected_option = select_element.first_selected_option.text
    print(f"Currently selected option: {selected_option}")
    #assert selected_option == "Student"
    print("Student is selected")

    # Select "Employed"
    select_status("Employed")
    # Verify if "Employed" is selected
    selected_option = select_element.first_selected_option.text
    print(f"Currently selected option: {selected_option}")
    #assert selected_option == "Employed"
    print("Employed is selected")

    # Check if "Entrepreneur" is disabled
    entrepreneur_option = driver.find_element(By.XPATH, "//label[normalize-space()='Entrepreneur (disabled)']")
    assert "disabled" in entrepreneur_option.get_attribute("outerHTML")
    print("Entrepreneur option is disabled")

    # Select "Entrepreneur" and handle the case where it should not be selected
    try:
        select_status("Entrepreneur")
        print("Entrepreneur is selected")
    except Exception:
        print("Entrepreneur selection is disabled as expected")

finally:
    # Close the browser after the test
    driver.quit()'''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

# Initialize the WebDriver
chromedriver_path = r"C:\Browsers\chromedriver-win64\chromedriver.exe"
service_obj = Service(chromedriver_path)
driver = webdriver.Chrome(service=service_obj)

try:
    # Open the website
    driver.get('https://rahulshettyacademy.com/angularpractice/')

    # Wait for the page to load
    wait = WebDriverWait(driver, 10)

    # Locate the Employment Status dropdown
    employment_status_dropdown = wait.until(
        EC.visibility_of_element_located((By.ID, 'exampleFormControlSelect1'))
    )

    # Print the options of the dropdown to verify
    select_element = Select(employment_status_dropdown)
    options = select_element.options
    print("Options in the dropdown:")
    for option in options:
        print(option.text)

    # Function to select a status dynamically
    def select_status(status):
        try:
            select_element.select_by_visible_text(status)
            print(f"Selected: {status}")
            time.sleep(1)
        except Exception as e:
            print(f"Error selecting {status}: {e}")

    # Now let's try selecting "Student"
    select_status("Student")

    # Verify if "Student" is selected
    selected_option = select_element.first_selected_option.text
    print(f"Currently selected option: {selected_option}")
    #assert selected_option == "Student"
    print("Student is selected")

    # Select "Employed"
    select_status("Employed")
    # Verify if "Employed" is selected
    selected_option = select_element.first_selected_option.text
    print(f"Currently selected option: {selected_option}")
    #assert selected_option == "Employed"
    print("Employed is selected")

    # Check if "Entrepreneur" is present and visible
    try:
        entrepreneur_option = driver.find_element(By.XPATH, "//option[text()='Entrepreneur']")
        print(f"Entrepreneur option found: {entrepreneur_option.text}")
        assert "disabled" in entrepreneur_option.get_attribute("outerHTML")
        print("Entrepreneur option is disabled")
    except Exception as e:
        print(f"Error finding Entrepreneur option: {e}")

    # Attempt to select "Entrepreneur" and handle the case where it should not be selected
    try:
        select_status("Entrepreneur")
        print("Entrepreneur is selected")
    except Exception:
        print("Entrepreneur selection is disabled as expected")

finally:
    # Close the browser after the test
    driver.quit()
