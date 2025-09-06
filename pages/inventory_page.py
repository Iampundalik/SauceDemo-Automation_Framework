from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):
    INVENTORY_CONTAINER = (By.ID, 'inventory_container')
    FIRST_ADD_TO_CART = (By.CSS_SELECTOR, 'button.btn_inventory')
    CART_BADGE = (By.CSS_SELECTOR, '.shopping_cart_badge')
    CART_LINK = (By.CSS_SELECTOR, 'a.shopping_cart_link')
    SORT_SELECT = (By.CSS_SELECTOR, 'select[data-test="product-sort-container"]')
    ITEM_PRICES = (By.CSS_SELECTOR, '.inventory_item_price')
    MENU_BTN = (By.CLASS_NAME, 'bm-burger-button')
    LOGOUT_LINK = (By.ID, 'logout_sidebar_link')

    def is_loaded(self):
        return self.is_visible(self.INVENTORY_CONTAINER)

    def add_first_item_to_cart(self):
        self.click(self.FIRST_ADD_TO_CART)

    def open_cart(self):
        self.click(self.CART_LINK)

    def set_sort(self, value):
        # value examples: 'lohi', 'hilo', 'az', 'za'
        from selenium.webdriver.support.ui import Select
        select = Select(self.driver.find_element(*self.SORT_SELECT))
        select.select_by_value(value)

    def get_prices(self):
        return [float(e.text.replace('$', '')) for e in self.driver.find_elements(*self.ITEM_PRICES)]

    def logout(self):
        self.click(self.MENU_BTN)
        self.click(self.LOGOUT_LINK)