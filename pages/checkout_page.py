from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    FIRST_NAME = (By.ID, 'first-name')
    LAST_NAME = (By.ID, 'last-name')
    POSTAL_CODE = (By.ID, 'postal-code')
    CONTINUE_BTN = (By.ID, 'continue')
    FINISH_BTN = (By.ID, 'finish')
    COMPLETE_HEADER = (By.CSS_SELECTOR, 'h2.complete-header')
    ERROR_MSG = (By.CSS_SELECTOR, 'h3[data-test="error"]')


    def fill_information(self, first, last, postal):
        if first:
            self.type(self.FIRST_NAME, first)
        if last:
            self.type(self.LAST_NAME, last)
        if postal:
            self.type(self.POSTAL_CODE, postal)

        # Always click Continue to trigger validation if fields are empty
        self.click(self.CONTINUE_BTN)

    def finish(self):
        self.click(self.FINISH_BTN)

    def is_complete(self):
        return self.is_visible(self.COMPLETE_HEADER)

    def get_error(self):
        return self.get_text(self.ERROR_MSG)
