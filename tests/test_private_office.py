
from conftest import *

email = '1@ya.ru'
password = '123456'

class TestClickPersonalAccount:
    def test_click_to_go_to_personal_account(self, driver):

        # Находим кнопку "Войти" и кликаем на неё
        driver.find_element(*Locators.button_login_account).click()

        # Находим поле "Email" и заполняем его
        driver.find_element(*Locators.email).send_keys(email)

        # Находим поле "Пароль" и заполняем его
        driver.find_element(*Locators.password).send_keys(password)

        # Находим кнопку "Войти" и кликаем на неё
        driver.find_element(*Locators.button_login).click()

        # Находим кнопку "Личный кабинет" и кликаем на неё
        driver.find_element(*Locators.button_personal_account).click()

        # Ждем загрузку личного кабинета
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Сохранить')]")))

        # Проверяем URL
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'
