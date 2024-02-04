from selenium.webdriver.common.by import By


class OrderPageLocators:
    NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']") # поле ввода имени
    SURNAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']") # поле ввода фамилии
    ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']") # поле ввода адреса
    FIELD_METRO = [By.XPATH, ".//input[@placeholder='* Станция метро']"]  # поле ввода метро
    CHOOSE_METRO = [By.XPATH, ".//li[@data-value={num}]"]  # выпадающий список станций метро
    PHONE_FIELD = (By.CSS_SELECTOR, "input[placeholder='* Телефон: на него позвонит курьер']") # поле ввода номера телефона
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']") # кнопка "Далее"
    FIELD_WHEN = [By.XPATH, ".//input[@placeholder='* Когда привезти самокат']"]  # поле ввода даты
    CHOOSE_DATE = (By.XPATH, ".//div[contains(@class, 'selected')]")  # выбранная дата в календаре
    RENT_FIELD = (By.CLASS_NAME, "Dropdown-root") # поле ввода срока аренды
    FIELD_LIMIT = [By.XPATH, ".//div[text()='* Срок аренды']"]  # поле срока аренды
    ONE_DAY_BUTTON = (By.XPATH, '//div[text() = "сутки"]')  # Кнопка "сутки"
    FOUR_DAYS_BUTTON = (By.XPATH, '//div[text() = "четверо суток"]')  # Кнопка "четверо суток"
    CHOOSE_SCOOTER = [By.XPATH, ".//label[contains(@class, 'Checkbox_Label')]"]  # выбор самоката
    BLACK_COLOR = (By.ID, "black") # выбор цвета самоката "Чёрный жемчуг"
    GREY_COLOR = (By.ID, "grey") # выбор цвета самоката "Серая безысходность"
    COMMENTS = (By.XPATH, "//input[@placeholder='Комментарий для курьера']") # выбор комментария
    ORDER_BUTTON = (By.XPATH, '//*[contains(@class,"Order_Buttons")]//button[text()="Заказать"]') # кнопка заказа
    YES_BUTTON = (By.XPATH, "//button[text()='Да']") # кнопка подтверждения
    STATUS_VIEW = (By.XPATH, ".//*[contains(@class,'Order_ModalHeader')]") # кнопка просмотра заказа