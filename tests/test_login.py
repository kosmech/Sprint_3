from conftest import *

email = '1@ya.ru'
password = '123456'

class TestLogin:
    def test_login_by_click_the_login_button_on_the_main_page(self, driver):

        # Находим кнопку "Войти" и кликаем на неё
        driver.find_element(*Locators.button_login_account).click()

        # Находим поле "Email" и заполняем его
        driver.find_element(*Locators.email).send_keys(email)

        # Находим поле "Пароль" и заполняем его
        driver.find_element(*Locators.password).send_keys(password)

        # Находим кнопку "Войти" и кликаем на неё
        driver.find_element(*Locators.button_login).click()

        # Ждем входа в аккаунт
        WebDriverWait(driver, 6).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Оформить заказ')]")))

        # Проверяем текст кнопки
        assert driver.find_element(*Locators.button_checkout).text == "Оформить заказ"

    def test_login_through_the_button_personal_account(self, driver):

        # Находим кнопку "Личный кабинет" и кликаем на неё
        driver.find_element(*Locators.button_personal_account).click()

        # Находим поле "Email" и заполняем его
        driver.find_element(*Locators.email).send_keys(email)

        # Находим поле "Пароль" и заполняем его
        driver.find_element(*Locators.password).send_keys(password)

        # Находим кнопку "Войти" и кликаем на неё
        driver.find_element(*Locators.button_login).click()

        # Ждем входа в аккаунт
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, "//button[contains(text(),'Оформить заказ')]")))

        # Проверяем текст кнопки
        assert driver.find_element(*Locators.button_checkout).text == "Оформить заказ"

    def test_login_through_the_button_in_the_registration_form(self, driver):

        # заходим на страницу регистрации
        driver.get(url + 'register')

        # Находим кнопку "Войти" на странице регистрации и кликаем на неё
        driver.find_element(*Locators.button_login_registration_page).click()

        # Находим поле "Email" и заполняем его
        driver.find_element(*Locators.email).send_keys(email)

        # Находим поле "Пароль" и заполняем его
        driver.find_element(*Locators.password).send_keys(password)

        # Находим кнопку "Войти" и кликаем на неё
        driver.find_element(*Locators.button_login).click()

        # Ждем входа в аккаунт
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, "//button[contains(text(),'Оформить заказ')]")))

        # Проверяем текст кнопки
        assert driver.find_element(*Locators.button_checkout).text == "Оформить заказ"

    def test_login_via_the_button_in_the_password_recovery_form(self, driver):

        # заходим на страницу входа в аккаунт
        driver.get(url + 'login')

        # Находим кнопку "Восстановить пароль" и кликаем на неё
        driver.find_element(*Locators.button_recovery_password).click()

        # Находим кнопку "Войти" и кликаем на неё
        driver.find_element(*Locators.button_login_registration_page).click()

        # Находим поле "Email" и заполняем его
        driver.find_element(*Locators.email).send_keys(email)

        # Находим поле "Пароль" и заполняем его
        driver.find_element(*Locators.password).send_keys(password)

        # Находим кнопку "Войти" и кликаем на неё
        driver.find_element(*Locators.button_login).click()

        # Ждем входа в аккаунт
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, "//button[contains(text(),'Оформить заказ')]")))

        # Проверяем текст кнопки
        assert driver.find_element(*Locators.button_checkout).text == "Оформить заказ"






