import time

import wait.log
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_date_picker_all():

    #Desired date
    target_date= 'October 28, 2030'
    target_month ="October"
    target_year = "2030"
    #Start browser
    driver = webdriver.Chrome()
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    driver.maximize_window()
    driver.find_element(By.CSS_SELECTOR, "svg[class*='react-date-picker__calendar-button__icon']").click()
    driver.implicitly_wait(5)
    # calling function for select date desired one.
    select_date(driver, target_date, target_month, target_year)





def select_date(driver, target_date, target_month, target_year):
    # Locators for react calendar navigation
    HEADER = (By.CSS_SELECTOR, "span[class^='react-calendar__navigation__label__labelText']")
    PREV_MONTH = (By.XPATH, "//button[contains(text(),'‹')]")
    NEXT_MONTH = (By.XPATH, "//button[contains(text(),'›')]")
    PREV_YEAR = (By.CSS_SELECTOR, "button[class='react-calendar__navigation__arrow react-calendar__navigation__prev2-button']")
    NEXT_YEAR = (By.CSS_SELECTOR, "button[class='react-calendar__navigation__arrow react-calendar__navigation__next2-button']")
    Dates_locator = (By.XPATH, "//button/abbr")

    MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
              'November', 'December']

    while True:
        header = driver.find_element(*HEADER).text
        current_month, current_year = header.split()
        current_year = int(current_year)

        if current_month == target_month and current_year == int(target_year):
            break

        if current_year < int(target_year):
            driver.find_element(*NEXT_YEAR).click()
            time.sleep(0.3)
            continue
        elif current_year > int(target_year):
            driver.find_element(*PREV_YEAR).click()
            time.sleep(0.3)
            continue

        if MONTHS.index(current_month) < MONTHS.index(target_month):
            driver.find_element(*NEXT_MONTH).click()
        else:
            driver.find_element(*PREV_MONTH).click()
            time.sleep(0.3)
    dates = driver.find_elements(*Dates_locator)
    for i in dates:
        get_date = i.get_attribute("aria-label")
        if get_date == target_date:
            i.click()
            print(f"selected targeted date: {get_date}")
            break

