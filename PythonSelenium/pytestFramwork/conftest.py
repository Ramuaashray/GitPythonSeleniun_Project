import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser selection"
    )



@pytest.fixture( scope="function" )
def browserinstance(request):
    global driver
    browser_name = request.config.getoption( "browser_name" )
    service_obj = Service()
    if browser_name == "chrome":  #firefox
        driver = webdriver.Chrome( service=service_obj )
    elif browser_name == "firefox":
        driver = webdriver.Firefox( service=service_obj )

    yield driver