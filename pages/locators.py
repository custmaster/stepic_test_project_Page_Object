from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
class LoginPageLocators():
	LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
	REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
class ProductPageLocators():
	BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
	NAME_PRODUCT = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
	PRICE_PRODUCT = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
	NAME_PRODUCT_IN_MESSAGE_ADD_TO_BASKET = (By.CSS_SELECTOR, ".alertinner strong")
	PRICE_PRODUCT_IN_MESSAGE_ADD_TO_BASKET = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
	SUCCESS_MESSAGE=(By.CSS_SELECTOR,".alert-success")
