from conftest import *

email = '1@ya.ru'
password = '123456'

class TestTransitionToConstructor:
    def test_transition_from_personal_account_click_to_go_to_constructor(self, driver):

        # Находим кнопку "Личный кабинет" и кликаем на неё
        driver.find_element(*Locators.button_personal_account).click()

        # Находим поле "Email" и заполняем его
        driver.find_element(*Locators.email).send_keys(email)

        # Находим поле "Пароль" и заполняем его
        driver.find_element(*Locators.password).send_keys(password)

        # Находим кнопку "Войти" и кликаем на неё
        driver.find_element(*Locators.button_login).click()

        # Находим кнопку "Личный кабинет" и кликаем на неё
        driver.find_element(*Locators.button_personal_account).click()

        # Находим кнопку "Конструктор" и кликаем на неё
        driver.find_element(*Locators.button_constructor).click()

        # Проверяем URL
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_transition_from_personal_account_click_to_go_to_logo(self, driver):

        # Находим кнопку "Личный кабинет" и кликаем на неё
        driver.find_element(*Locators.button_personal_account).click()

        # Находим поле "Email" и заполняем его
        driver.find_element(*Locators.email).send_keys(email)

        # Находим поле "Пароль" и заполняем его
        driver.find_element(*Locators.password).send_keys(password)

        # Находим кнопку "Войти" и кликаем на неё
        driver.find_element(*Locators.button_login).click()

        # Находим кнопку "Личный кабинет" и кликаем на неё
        driver.find_element(*Locators.button_personal_account).click()

        # Находим лого и кликаем на него
        driver.find_element(*Locators.logo).click()

        # Проверяем URL
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'


