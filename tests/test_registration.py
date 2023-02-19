from conftest import *
import random

class TestRegistration:
    def test_registration_with_valid_data(self, driver):

        # заходим на страницу регистрации
        driver.get(url + 'register')

        # Находим поле "Имя" и заполняем его
        driver.find_element(*Locators.name).send_keys('Konstantin')

        # Генерация email
        q = random.randint(100, 999)
        generation_email = f'konstantin_mechik_6_{q}@ya.ru'

        # Находим поле "Email" и заполняем его
        driver.find_element(*Locators.email).send_keys(generation_email)

        # Находим поле "Пароль" и заполняем его
        driver.find_element(*Locators.password).send_keys('123456')

        # Находим кнопку "Зарегистрироваться" и кликаем по ней
        driver.find_element(*Locators.button_registration).click()

        # Ждем загрузки страницы с "Вход"
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.title_login_page))

        # Проверяем URL
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    def test_registration_with_no_valid_password(self, driver):

        # заходим на страницу регистрации
        driver.get(url + 'register')

        # Находим поле "Имя" и заполняем его
        driver.find_element(*Locators.name).send_keys('Konstantin')

        # Генерация email
        q = random.randint(100, 999)
        generation_email = f'konstantin_mechik_6_{q}@ya.ru'

        # Находим поле "Email" и заполняем его
        driver.find_element(*Locators.email).send_keys(generation_email)

        # Находим поле "Пароль" и заполняем его не валидным паролем
        driver.find_element(*Locators.password).send_keys('12345')

        # Находим кнопку "Зарегистрироваться" и кликаем по ней
        driver.find_element(*Locators.button_registration).click()

        # Проверяем появление ошибки о неправильном пароле
        assert driver.find_element(*Locators.alert_password_fail)