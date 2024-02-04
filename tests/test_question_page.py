import allure
import pytest
from conftest import driver
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
from data import Answer


class TestQuestionsPage:
    @allure.title('Проверка выпадающего списка в разделе "Вопросы о важном"')
    @allure.description('Проверяем, что при нажатии на стрелочку в разделе «Вопросы о важном» будут развёрнуты ответы')
    @pytest.mark.parametrize('question, answer, right_answer',
                             [
                                 (MainPageLocators.FIRST_QUESTION, MainPageLocators.FIRST_ANSWER, Answer.first_answer),
                                 (MainPageLocators.SECOND_QUESTION, MainPageLocators.SECOND_ANSWER, Answer.second_answer),
                                 (MainPageLocators.THIRD_QUESTION, MainPageLocators.THIRD_ANSWER, Answer.third_answer),
                                 (MainPageLocators.FOURTH_QUESTION, MainPageLocators.FOURTH_ANSWER, Answer.fourth_answer),
                                 (MainPageLocators.FIFTH_QUESTION, MainPageLocators.FIFTH_ANSWER, Answer.fifth_answer),
                                 (MainPageLocators.SIXTH_QUESTION, MainPageLocators.SIXTH_ANSWER, Answer.sixth_answer),
                                 (MainPageLocators.SEVENTH_QUESTION, MainPageLocators.SEVENTH_ANSWER, Answer.seventh_answer),
                                 (MainPageLocators.EIGHTH_QUESTION, MainPageLocators.EIGHTH_ANSWER, Answer.eighth_answer)
                             ])
    def test_answers_to_questions(self, driver, question, answer, right_answer):
            main_page = MainPage(driver)
            main_page.click_to_cookie_button()
            main_page.find_questions()
            main_page.click_element(question)
            main_page.wait_for_element(answer)
            right_text = main_page.get_element_text(answer)
            assert right_text == right_answer
