from selenium.webdriver.common.by import By


class MainPageLocators:
    ORDER_TOP_BUTTON = (By.CLASS_NAME, 'Button_Button__ra12g')  # Верхняя кнопка "Заказать"
    ORDER_DOWN_BUTTON = (By.XPATH, '//div[@class="Home_FinishButton__1_cWm"]/button')  # Нижняя кнопка "Заказать"
    YANDEX_LOGO = (By.CLASS_NAME, 'Header_LogoYandex__3TSOI')  # Логотип "Яндекс"
    SCOOTER_LOGO = [By.CLASS_NAME, 'Header_LogoScooter__3lsAR'] # Логотип "Самокат"
    COOKIE_BUTTON = (By.ID, 'rcc-confirm-button') # Кнопка Куки
    DZEN_HEADER = [By.ID, "dzen-header"]  # заголовок на странице дзена
    IMPORTANT_QUESTION = [By.XPATH, ".//div[text()='Вопросы о важном']"]  # блок с вопросами о важном
    # вопросы
    FIRST_QUESTION = [By.ID, 'accordion__heading-0'] # перый вопрос
    SECOND_QUESTION = [By.ID, 'accordion__heading-1'] # второй вопрос
    THIRD_QUESTION = [By.ID, 'accordion__heading-2'] # третий вопрос
    FOURTH_QUESTION = [By.ID, 'accordion__heading-3'] # четвёртый вопрос
    FIFTH_QUESTION = [By.ID, 'accordion__heading-4'] # пятый вопрос
    SIXTH_QUESTION = [By.ID, 'accordion__heading-5'] # шестой вопрос
    SEVENTH_QUESTION = [By.ID, 'accordion__heading-6'] # седьмой вопрос
    EIGHTH_QUESTION = [By.ID, 'accordion__heading-7'] # восьмой вопрос
    # ответы
    FIRST_ANSWER = [By.ID, 'accordion__panel-0'] # первый ответ
    SECOND_ANSWER = [By.ID, 'accordion__panel-1'] # второй ответ
    THIRD_ANSWER = [By.ID, 'accordion__panel-2'] # третий ответ
    FOURTH_ANSWER = [By.ID, 'accordion__panel-3'] # четвёртый ответ
    FIFTH_ANSWER = [By.ID, 'accordion__panel-4'] # пятый ответ
    SIXTH_ANSWER = [By.ID, 'accordion__panel-5'] # шестой ответ
    SEVENTH_ANSWER = [By.ID, 'accordion__panel-6'] # седьмой ответ
    EIGHTH_ANSWER = [By.ID, 'accordion__panel-7'] # восьмой ответ

