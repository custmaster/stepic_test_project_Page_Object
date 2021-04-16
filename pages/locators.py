from selenium.webdriver.common.by import By


class BasePageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
	LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
	BTN_GO_TO_BASKET = (By.CSS_SELECTOR, ".btn-group .btn.btn-default")
class BasketPageLocators():
	MESSAGE_THAT_BASKET_IS_EMPTY = (By.CSS_SELECTOR, "div #content_inner > p")
	PRODUCT_IN_BASKET = (By.CSS_SELECTOR, ".basket-items")
class MainPageLocators():
    pass
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
