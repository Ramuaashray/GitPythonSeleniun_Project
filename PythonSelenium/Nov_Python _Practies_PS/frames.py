from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chromedriver_path = r"C:\Browsers\chromedriver-win64\chromedriver.exe"
service_obj1 =Service(chromedriver_path)
driver = webdriver.Chrome(service=service_obj1)
driver.implicitly_wait(5)


driver.get("https://the-internet.herokuapp.com/nested_frames")
driver.maximize_window()
driver.switch_to.frame("/frame_left")
print(driver.find_element(By.CSS_SELECTOR, "frame[name='frame-left']").text)