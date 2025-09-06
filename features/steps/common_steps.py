from behave import given, when, then
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import config

@given('I am on the SauceDemo login page')
def step_impl(context):
    context.login = LoginPage(context.driver)
    context.inventory = InventoryPage(context.driver)
    context.cart = CartPage(context.driver)
    context.checkout = CheckoutPage(context.driver)
    context.login.open(config.BASE_URL)

@given('I am logged in as "{user}" with password "{pwd}"')
def step_impl(context, user, pwd):
    context.login = LoginPage(context.driver)
    context.inventory = InventoryPage(context.driver)
    context.cart = CartPage(context.driver)
    context.checkout = CheckoutPage(context.driver)
    context.login.open(config.BASE_URL)
    context.login.login(user, pwd)
    assert context.inventory.is_loaded(), "Inventory page did not load after login"

@when('I logout from the application')
def step_impl(context):
    context.inventory = getattr(context, 'inventory', InventoryPage(context.driver))
    context.inventory.logout()

@then('I should see the login page')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    )
    assert "Logout Sucessfull"
