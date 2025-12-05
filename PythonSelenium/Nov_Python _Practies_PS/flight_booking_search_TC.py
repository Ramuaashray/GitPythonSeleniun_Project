import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_flight_search():
    target_month = "May"
    target_year = "2022"


    NEXT_YEAR =(By.CSS_SELECTOR, "span[class='ui-icon ui-icon-circle-triangle-e']")
    PREV_YEAR = (By.CSS_SELECTOR, "span[class='ui-icon ui-icon-circle-triangle-w']")
    Dates_locator = (By.XPATH, "//div/table/tbody/tr/td")
    # Start browser
    driver = webdriver.Chrome()
    driver.get("https://rahulshettyacademy.com/dropdownsPractise/#")
    driver.maximize_window()
    driver.find_element(By.ID, "autosuggest").send_keys("India")
    time.sleep(3)
    countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
    print(len(countries))
    for country in countries:
        if country.text == "India":
            country.click()
            break

    departure_city = driver.find_element(By.XPATH, "//input[@id='ctl00_mainContent_ddl_originStation1_CTXT']")
    departure_city.click()
    departure_city.send_keys("BLR")

    arrival_city =driver.find_element(By.XPATH, "//input[@id='ctl00_mainContent_ddl_destinationStation1_CTXT']")
    arrival_city.click()
    time.sleep(3)
    arrival_city.send_keys("Mum")



    while True:
        current_year = driver.find_element(By.CSS_SELECTOR, "span[class='ui-datepicker-year']").text
        current_month = driver.find_element(By.CSS_SELECTOR, "span[class='ui-datepicker-month']").text
        MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                  'November', 'December']

        if current_month == target_month and current_year == target_year:
            break

        if current_year < target_year:
            driver.find_element(*NEXT_YEAR).click()
            time.sleep(0.3)
            continue
        elif current_year > target_year:
            driver.find_element(*PREV_YEAR).click()
            time.sleep(0.3)
            continue
        if MONTHS.index(current_month) < MONTHS.index(target_month):
            driver.find_element(*NEXT_YEAR).click()
        else:
            driver.find_element(*PREV_YEAR).click()
            time.sleep(0.3)
    dates = driver.find_elements(*Dates_locator)
    for i in dates:
        #get_date = i.get_attribute("aria-label")
        j = i.text
        if j == '9':
            i.click()
            print(f"selected targeted date:{j},{target_month},{target_year}")
            break

    driver.find_element(By.ID, "divpaxinfo").click()
    time.sleep(2)
    adults = driver.find_element(By.XPATH, "(//span[@id='hrefIncAdt'])[1]")
    adults.click()
    adults.click()
    driver.find_element(By.CSS_SELECTOR, "input[value='Done']").click()
    driver.find_element(By.ID, "ctl00_mainContent_DropDownListCurrency").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "option[value='AED']").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "input[id='ctl00_mainContent_btn_FindFlights']").click()


def test_flight_round_trip_tc():
    target_month = "June"
    target_year = "2020"
    #target_day ='9'

    NEXT_YEAR = (By.CSS_SELECTOR, "span[class='ui-icon ui-icon-circle-triangle-e']")
    PREV_YEAR = (By.CSS_SELECTOR, "span[class='ui-icon ui-icon-circle-triangle-w']")
    Dates_locator = (By.XPATH, "//div/table/tbody/tr/td")
    # Start browser
    driver = webdriver.Chrome()
    driver.get("https://rahulshettyacademy.com/dropdownsPractise/#")
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.find_element(By.ID, "autosuggest").send_keys("India")

    countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
    print(len(countries))
    for country in countries:
        if country.text == "India":
            country.click()
            break

    driver.find_element(By.CSS_SELECTOR, "#ctl00_mainContent_chk_IndArm").click()
    tooltip = driver.find_element(By.CSS_SELECTOR,"div[id='ctl00_mainContent_IndArm'] span[class='search-offer-tooltip mobile-tooltip-left']").text
    print(tooltip)

    driver.find_element(By.CSS_SELECTOR, "input[id='ctl00_mainContent_rbtnl_Trip_1']").click()
    departure_city = driver.find_element(By.XPATH, "//input[@id='ctl00_mainContent_ddl_originStation1_CTXT']")
    departure_city.click()
    departure_city.send_keys("BLR")

    arrival_city = driver.find_element(By.XPATH, "//input[@id='ctl00_mainContent_ddl_destinationStation1_CTXT']")
    arrival_city.click()
    time.sleep(3)
    arrival_city.send_keys("Mum")

    # calling function selection departure date
    Calendar_date_Selection(driver, target_month, target_year, NEXT_YEAR, PREV_YEAR, Dates_locator, '9')
    driver.find_element(By.XPATH, "(//button[@type='button'])[2]").click()
    #calling function selection arrival date
    Calendar_date_Selection(driver, "August", target_year,NEXT_YEAR,PREV_YEAR, Dates_locator, '28')

    driver.find_element(By.ID, "divpaxinfo").click()
    adults = driver.find_element(By.XPATH, "(//span[@id='hrefIncAdt'])[1]")
    adults.click()
    adults.click()
    driver.find_element(By.CSS_SELECTOR, "input[value='Done']").click()
    driver.find_element(By.ID, "ctl00_mainContent_DropDownListCurrency").click()
    driver.find_element(By.CSS_SELECTOR, "option[value='AED']").click()
    driver.find_element(By.CSS_SELECTOR, "input[id='ctl00_mainContent_btn_FindFlights']").click()


def Calendar_date_Selection(driver, target_month, target_year,NEXT_YEAR,PREV_YEAR, Dates_locator, target_day):
    while True:
        current_year = driver.find_element(By.CSS_SELECTOR, "span[class='ui-datepicker-year']").text
        current_month = driver.find_element(By.CSS_SELECTOR, "span[class='ui-datepicker-month']").text
        MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                  'November', 'December']

        if current_month == target_month and current_year == target_year:
            break

        if current_year < target_year:
            driver.find_element(*NEXT_YEAR).click()
            time.sleep(0.3)
            continue
        elif current_year > target_year:
            driver.find_element(*PREV_YEAR).click()
            time.sleep(0.3)
            continue
        if MONTHS.index(current_month) < MONTHS.index(target_month):
            driver.find_element(*NEXT_YEAR).click()
        else:
            driver.find_element(*PREV_YEAR).click()
            time.sleep(0.3)
    dates = driver.find_elements(*Dates_locator)
    for i in dates:
        # get_date = i.get_attribute("aria-label")
        j = i.text
        if j == target_day:
            i.click()
            print(f"selected targeted date:{j},{target_month},{target_year}")
            break





