from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def test_web_table():
    chromedriver_path = r"C:\Browsers\chromedriver-win64\chromedriver.exe"
    service_obj1 = Service(chromedriver_path)
    driver = webdriver.Chrome(service=service_obj1)
    driver.implicitly_wait(5)

    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    driver.maximize_window()


