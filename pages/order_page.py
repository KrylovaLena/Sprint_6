import allure
import random
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step("Заполнить поле 'Имя'")
    def set_name(self, name):
        self.set_text_to_element(OrderPageLocators.NAME_FIELD, name)

    @allure.step("Заполнить поле 'Фамилия'")
    def set_surname(self, surname):
        self.set_text_to_element(OrderPageLocators.SURNAME_FIELD, surname)

    @allure.step("Заполнить поле 'Адрес'")
    def set_address(self, address):
        self.set_text_to_element(OrderPageLocators.ADDRESS_FIELD, address)

    @allure.step("Кликнуть по полю 'Метро'")
    def click_to_metro(self):
        self.click_element(OrderPageLocators.FIELD_METRO)

    @allure.step("Выбрать станцию метро из выпадающего списка")
    def choose_metro_station(self):
        method, locator = OrderPageLocators.CHOOSE_METRO
        number = random.randint(1, 112)
        locator = locator.format(num=number)
        self.click_element((method, locator))

    @allure.step("Заполнить поле 'Телефон'")
    def set_phone(self, phone):
        self.set_text_to_element(OrderPageLocators.PHONE_FIELD, phone)

    @allure.step("Нажать на кнопкку 'Далее'")
    def click_next_button(self):
        self.click_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Кликнуть по полю 'Когда привезти самокат'")
    def set_date_to_field(self, text):
        self.set_text_to_element(OrderPageLocators.FIELD_WHEN, text)

    @allure.step("Кликнуть выбранную дату в календаре")
    def click_to_choose_date(self):
        self.click_element(OrderPageLocators.CHOOSE_DATE)

    @allure.step("Кликнуть по полю 'Срок аренды'")
    def click_to_rent_date(self):
        self.click_element(OrderPageLocators.FIELD_LIMIT)

    @allure.step("Выбрать вариант из выпадающего списка 'Срок аренды'")
    def choose_date(self, days_button):
        self.click_element(days_button)


    @allure.step("Выбрать 'Цвет самоката'")
    def click_colour(self, colour):
        self.click_element(colour)

    @allure.step("Заполнить поле 'Комментарий'")
    def set_comment(self, comment):
        self.set_text_to_element(OrderPageLocators.COMMENTS, comment)

    @allure.step('Нажать кнопку "да"')
    def click_button_yes(self):
        self.click_element(OrderPageLocators.YES_BUTTON)

    @allure.step('Нажать на кнопку "Заказать"')
    def click_order(self):
        self.click_element(OrderPageLocators.ORDER_BUTTON)

    @allure.step('Получить всплывающее окно с номером заказа "Заказ оформлен"')
    def get_success_order_text(self):
        return self.get_element_text(OrderPageLocators.STATUS_VIEW)

    @allure.step('Заполнить форму с данными пользователя')
    def fill_rent_form(self, name, surname, address, phone, date, days_button, colour, comment):
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.click_to_metro()
        self.choose_metro_station()
        self.set_phone(phone)
        self.click_next_button()
        self.set_date_to_field(date)
        self.click_to_choose_date()
        self.click_to_rent_date()
        self.choose_date(days_button)
        self.click_colour(colour)
        self.set_comment(comment)
        self.click_order()
        self.click_button_yes()