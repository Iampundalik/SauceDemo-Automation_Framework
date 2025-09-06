from behave import when, then
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@when('I login with username "{user}" and password "{pwd}"')
def step_impl(context, user, pwd):
    context.login = getattr(context, 'login', LoginPage(context.driver))
    context.login.login(user, pwd)

@then('I should see the inventory page')
def step_impl(context):
    context.inventory = getattr(context, 'inventory', InventoryPage(context.driver))
    assert context.inventory.is_loaded(), "Inventory not visible"

@then('I should see an error containing "{expected}"')
def step_impl(context, expected):
    context.login = getattr(context, 'login', LoginPage(context.driver))
    err = context.login.get_error()
    assert expected in err, f"Expected '{expected}' in error '{err}'"
