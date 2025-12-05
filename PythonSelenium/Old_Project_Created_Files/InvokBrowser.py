#import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#service_obj = Service("C:\selenium\chromedriver")
#service_obj = Service("C:\selenium\pythonBrowser\chromedriver")
#driver = webdriver.Chrome(service=service_obj)


driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com")


# Remember to close the driver when done
#driver.quit()







'''import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Use raw string literal for the path (or double backslashes)
service_obj = Service(r"C:\selenium\pythonBrowser\chromedriver")

# Create the driver object using the service
driver = webdriver.Chrome(service=service_obj)

# Navigate to the URL
driver.get("https://rahulshettyacademy.com")

# Remember to close the driver when done
driver.quit()'''





















#time.sleep(2)