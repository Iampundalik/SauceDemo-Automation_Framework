from behave import when, then
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@when('I add the first item to the cart')
def step_impl(context):
    context.inventory = getattr(context, 'inventory', InventoryPage(context.driver))
    context.inventory.add_first_item_to_cart()
    # open cart afterwards
    context.inventory.open_cart()

@when('I proceed to checkout with "{first}" "{last}" "{postal}"')
def step_impl(context, first, last, postal):
    context.cart = getattr(context, 'cart', CartPage(context.driver))
    context.cart.checkout()
    context.checkout = getattr(context, 'checkout', CheckoutPage(context.driver))
    # Treat empty string as None to trigger validation
    f = first if first else None
    l = last if last else None
    p = postal if postal else None
    context.checkout.fill_information(f, l, p)
    # finish only if we reached overview
    try:
        context.checkout.finish()
    except Exception:
        pass

@when('I proceed to checkout with all fields blank')
def step_impl(context):
    context.cart = getattr(context, 'cart', CartPage(context.driver))
    context.cart.checkout()
    context.checkout = getattr(context, 'checkout', CheckoutPage(context.driver))
    context.checkout.fill_information("", "", "")   # Pass empty strings

@then('I should see the order completion page')
def step_impl(context):
    assert context.checkout.is_complete(), "Order completion header not visible"

@then('I should see a checkout error containing "{msg}"')
def step_impl(context, msg):
    err = context.checkout.get_error()
    assert msg in err, f"Expected '{msg}' in '{err}'"
