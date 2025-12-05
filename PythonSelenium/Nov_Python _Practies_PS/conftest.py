import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser selection"
    )


@pytest.fixture(scope="function")
def browserInstance(request):
    broweser_name = request.config.getoption("browser_name") # -- is not required why get option retrieving
    chromedriver_path = r"C:\Browsers\chromedriver-win64\chromedriver.exe"
    service_obj1 = Service(chromedriver_path)
    if broweser_name == "chrome":
        driver = webdriver.Chrome(service=service_obj1)
    elif broweser_name == "firefox":
        driver = webdriver.Firefox(service=service_obj1)
    driver.implicitly_wait(5)
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    driver.maximize_window()
    yield driver
    driver.close()