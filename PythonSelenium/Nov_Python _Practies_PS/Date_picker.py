import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_date_picker():
    driver = webdriver.Chrome()
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    driver.maximize_window()
    driver.find_element(By.CSS_SELECTOR, "svg[class*='react-date-picker__calendar-button__icon']").click()
    driver.implicitly_wait(5)

    date = "January 25, 2028"
    month_year = "January 2028"
    for c in range(12):
        month = driver.find_element(By.CSS_SELECTOR, "span[class^='react-calendar__navigation__label__labelText']").text
        if month == month_year:
            #dates = driver.find_elements(By.CSS_SELECTOR, "div[class='react-calendar__month-view__days'] button")
            dates = driver.find_elements(By.XPATH, "//button/abbr")
            for i in dates:
                #text = date_element.text
                # print(text)
                get_date = i.get_attribute("aria-label")
                if get_date == 'January 25, 2028':
                    i.click()
                    print(f"clicked {date}")
                    break
            break
        else:
            arrow_button = driver.find_element(By.CSS_SELECTOR, "button[class='react-calendar__navigation__arrow react-calendar__navigation__next2-button']")
            arrow_button.click()
            #month_arrow = driver.find_element(By.XPATH, "//button[contains(text(),'›')]")
            #month_arrow.click()
            time.sleep(5)


    print("Date selected successfully!")
    driver.close()

