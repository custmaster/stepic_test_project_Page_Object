from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasketPageLocators


class BasketPage(BasePage):
	
	def check_that_the_basket_is_empty(self):
		assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET), "Basket is not empty!"

	
	def check_reports_that_the_basket_is_empty(self):
		assert self.is_element_present(*BasketPageLocators.MESSAGE_THAT_BASKET_IS_EMPTY), "No massege!"

