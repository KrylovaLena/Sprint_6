import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step("Нажать на логотип 'Яндекс'")
    def click_logo_yandex(self):
        self.click_element(MainPageLocators.YANDEX_LOGO)

    @allure.step("Нажать на логотип 'Самокат'")
    def click_logo_scooter(self):
        self.click_element(MainPageLocators.SCOOTER_LOGO)

    @allure.step("Переключиться на новое окно и ожидаем, что открылась новая вкладка Дзен")
    def check_redirect_dzen(self):
        self.switch_to_new_window()
        return self.wait_for_element(MainPageLocators.DZEN_HEADER)

    @allure.step("Принять использование cookie,кликнув по кнопке 'да все привыкли'")
    def click_to_cookie_button(self):
        self.click_element(MainPageLocators.COOKIE_BUTTON)

    @allure.step("Проскроллить до блока 'Вопросы о важном'")
    def find_questions(self):
        element = self.driver.find_element(*MainPageLocators.FIRST_QUESTION)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Нажать на верхнюю кнопкку 'Заказать'")
    def click_order_top(self):
        self.click_element(MainPageLocators.ORDER_TOP_BUTTON)

    @allure.step("Нажать на нижнюю кнопкку 'Заказать'")
    def click_order_down(self):
        self.click_element(MainPageLocators.ORDER_DOWN_BUTTON)