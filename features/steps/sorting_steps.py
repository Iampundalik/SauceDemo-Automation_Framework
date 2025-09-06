from behave import when, then
from pages.inventory_page import InventoryPage

@when('I sort products by "{value}"')
def step_impl(context, value):
    context.inventory = getattr(context, 'inventory', InventoryPage(context.driver))
    context.inventory.set_sort(value)

@then('the product prices should be in ascending order')
def step_impl(context):
    prices = context.inventory.get_prices()
    assert prices == sorted(prices), f"Prices not sorted ascending: {prices}"
