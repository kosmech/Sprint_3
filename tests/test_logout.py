from conftest import *

email = '1@ya.ru'
password = '123456'

class TestLogout:
    def test_log_out_by_clicking_the_log_out_button_in_account(self, driver):

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
            expected_conditions.visibility_of_element_located(Locators.button_exit))

        # Находим кнопку "Выход" и кликаем на неё
        driver.find_element(*Locators.button_exit).click()

        # Ждем выхода из кабинета
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'Вход')]")))

        # Проверяем URL
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'