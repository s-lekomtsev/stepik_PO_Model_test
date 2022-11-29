import pytest
import faker
import time

from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage

# класс для user
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = page = LoginPage(browser, link)
        page.open()
        f = faker.Faker()
        email = f.email()
        password = str(time.time())
        page.register_new_user(email=email, password=password)
        time.sleep(10)
        page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        # проверка наличия сообщения
        # page.should_not_be_success_message()

        # находим и сохраняем название продукта и цену
        NameProduct = page.find_product()
        ProductPrice = page.find_product_price()

        # добавляем продукт в корзину
        page.add_to_basket_page()
        page.solve_quiz_and_get_code()

        time.sleep(10)
        # проверка наличия сообщения
        # page.should_not_be_success_message()
        page.is_disappeared_success_message()

        # сравним
        print()
        print(page.find_product_basket())
        print(NameProduct)
        page.comparison_name(name1=NameProduct, name2=page.find_product_basket())

        print(page.find_price_basket())
        print(ProductPrice)
        page.comparison_price(price1=ProductPrice, price2=page.find_price_basket())

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, link):

    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    # проверка наличия сообщения
    # page.should_not_be_success_message()

    # находим и сохраняем название продукта и цену
    NameProduct = page.find_product()
    ProductPrice = page.find_product_price()

    # добавляем продукт в корзину
    page.add_to_basket_page()
    page.solve_quiz_and_get_code()

    # проверка наличия сообщения
    # page.should_not_be_success_message()
    page.is_disappeared_success_message()

    # сравним
    print()
    print(page.find_product_basket())
    print(NameProduct)

    assert NameProduct+" has been added to your basket." == page.find_product_basket(), print("ERROR")
    print("ОК")

    print(page.find_price_basket())
    print(ProductPrice)

    assert "Your basket total is now "+ProductPrice == page.find_price_basket(), print("ERROR")
    print("ОК")

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasketPage(browser, link)
    page.open()

    page.go_to_basket()

    page.should_not_be_product_in_basket()

    assert page.find_basket_is_empty_text() != '', print("ERROR")
    print(page.find_basket_is_empty_text())

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


