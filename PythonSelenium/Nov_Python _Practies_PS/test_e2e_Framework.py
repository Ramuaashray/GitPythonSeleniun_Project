import json

import pytest

from PageObjects.login import LoginPage
test_data_path = '../Data/test_e2e_Framework.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

@pytest.mark.smoke
@pytest.mark.parametrize("test_list_item", test_list)
def test_e2e(browserInstance,test_list_item):
    driver = browserInstance
    loginpage = LoginPage(driver)
    shop_page =loginpage.login(test_list_item["userEmail"], test_list_item["userPassword"])
    shop_page.add_product_to_cart(test_list_item["productName"])
    checkout_confirmation = shop_page.goToCart()
    checkout_confirmation.checkout()
    checkout_confirmation.enter_delivery_address("China")
    checkout_confirmation.validate_order()
