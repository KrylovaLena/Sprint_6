import allure
import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:

    """Инициализация класса."""
    def __init__(self, driver):
        self.driver = driver

    """Выполнение клика по элементу на странице."""
    @allure.step('Кликаем по элементу {locator}')
    def click_element(self, locator):
        WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(locator))
        time.sleep(2)
        self.driver.find_element(*locator).click()

    """Получение текста элемента на странице."""
    def get_element_text(self, locator):
        element = WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        return element.text

    """Ввод текста в элемент на странице."""
    def set_text_to_element(self, locator, text):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).send_keys(text)

    def wait_for_element(self, locator):
        return WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(locator))


    """Поиск всех элементов на странице, соответствующих заданному локатору."""
    def find_option_elements(self, locator):
        return WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_all_elements_located(locator))

    """Ожидание загрузки сайта."""
    @allure.step('Открывем страницу {url}')
    def wait_for_site_to_load(self, url):
        WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be(url))

    """Возвращение текущего URL сайта."""
    def get_current_site(self):
        return self.driver.current_url

    """Переключение на новое окно браузера."""
    def switch_to_new_window(self):
        return self.driver.switch_to.window(self.driver.window_handles[1])


