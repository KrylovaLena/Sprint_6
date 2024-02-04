import allure
from conftest import driver
from pages.main_page import MainPage

from data import Site


class TestLogoPage:

    @allure.title('Проверка перехода на страницу "Дзен"')
    @allure.description('Нажимаем на логотип "Яндекс" и проверяем, что произошёл переход на главную страницу "Дзен"')
    def test_transition_to_dzen(self, driver):
        main_page = MainPage(driver)
        main_page.click_to_cookie_button()
        main_page.click_logo_yandex()
        assert main_page.check_redirect_dzen()

    @allure.title('Проверка перехода на главную страницу "Самокат"')
    @allure.description('Нажимаем на логотип "Самокат" и проверяем, что произошёл переход на главную страницу "Самоката"')
    def test_transition_to_scooter(self, driver):
        main_page = MainPage(driver)
        main_page.click_to_cookie_button()
        main_page.click_order_top()
        main_page.click_logo_scooter()
        main_page.wait_for_site_to_load(Site.main_site)
        assert main_page.get_current_site() == Site.main_site