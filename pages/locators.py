from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.XPATH, ".//*[@class='btn btn-default' and contains(@href, '/basket/')]")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_EMPTY = (By.XPATH, ".//div[@id='content_inner']")
    BASKET_PRODUCT = (By.XPATH, ".//div[@class='basket-title hidden-xs']")

class LoginPageLocators():
    LOGIN_URL = ()
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.NAME, "registration-email")
    REGISTER_PASS1 = (By.NAME, "registration-password1")
    REGISTER_PASS2 = (By.NAME, "registration-password2")
    REGISTER_BTN = (By.NAME, "registration_submit")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class ProductPageLocators():
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, "#add_to_basket_form")
    PRODUCT_MAIN = (By.XPATH, ".//*[@class='col-sm-6 product_main']/h1")
    PRODUCT_PRICE = (By.XPATH, ".//*[@class='col-sm-6 product_main']/p")
    PRODUCT_BASKET = (By.XPATH, ".//*[@class='alert alert-safe alert-noicon alert-success  fade in'][1]/div")
    PRODUCT_BASKET_PRICE = (By.XPATH, ".//*[@class='alert alert-safe alert-noicon alert-info  fade in']/div/p[1]")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(1)")


