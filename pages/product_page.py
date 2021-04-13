from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators


class ProductPage(BasePage):
	def add_product_to_basket(self):
		btn_add_to_basket = self.browser.find_element(
			*ProductPageLocators.BTN_ADD_TO_BASKET)
		btn_add_to_basket.click()
	def check_nane_product_in_massage_add_to_basket(self):
		name_product = self.browser.find_element(
			*ProductPageLocators.NAME_PRODUCT).text
		name_product_in_basket = self.browser.find_element(
			*ProductPageLocators.NAME_PRODUCT_IN_MESSAGE_ADD_TO_BASKET).text
		assert name_product == name_product_in_basket, "Product name does not match"
	def check_price_product_in_massage_add_to_basket(self):
		price_product = self.browser.find_element(
			*ProductPageLocators.PRICE_PRODUCT).text
		price_product_in_basket = self.browser.find_element(
			*ProductPageLocators.PRICE_PRODUCT_IN_MESSAGE_ADD_TO_BASKET).text
		assert price_product == price_product_in_basket, "Product price does not match"
	def should_not_be_success_massage(self):
		assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"
	def should_is_disappeared(self):
		assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Element has not disappeared"
