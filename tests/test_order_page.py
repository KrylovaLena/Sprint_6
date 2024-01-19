import allure
from conftest import driver
from pages.order_page import OrderPage
from pages.main_page import MainPage
from locators.order_page_locators import OrderPageLocators
from data import OrderData

data = OrderData()

class TestOrderPage:

    @allure.title('Проверка заказа через верхнюю кнопку "Заказать"')
    @allure.description("Проверка успешного заказа самоката через кнопку 'Заказать' в хедере")
    def test_create_order_order_button_header_success(self, driver):
        main_page = MainPage(driver)
        main_page.click_to_cookie_button()
        main_page.click_order_top()

        order_page = OrderPage(driver)
        order_page.fill_rent_form(data.name, data.surname, data.address, data.phone, data.date,
                                  OrderPageLocators.FOUR_DAYS_BUTTON, OrderPageLocators.GREY_COLOR, data.comment)
        assert 'Заказ оформлен' in OrderPage(driver).get_success_order_text()

    @allure.title('Проверка заказа через нижнюю кнопку "Заказать"')
    @allure.description("Проверка успешного заказа самоката через кнопку 'Заказать' внизу главной страницы")
    def test_create_order_order_button_down_success(self, driver):
        main_page = MainPage(driver)
        main_page.click_to_cookie_button()
        main_page.click_order_down()

        order_page = OrderPage(driver)
        order_page.fill_rent_form(data.name, data.surname, data.address, data.phone, data.date,
                                  OrderPageLocators.ONE_DAY_BUTTON, OrderPageLocators.BLACK_COLOR, data.comment)
        assert 'Заказ оформлен' in OrderPage(driver).get_success_order_text()
