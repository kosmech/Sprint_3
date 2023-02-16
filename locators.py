import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

class Locators:

    # поле для ввода имени
    name = (By.XPATH, "//input[@name = 'name']")

    # поле для ввода email
    email = (By.XPATH, "//label[text()='Email']/following-sibling::input")

    # поле для ввода password
    password = (By.XPATH, "//input[@name = 'Пароль']")

    # кнопка для регистрации
    button_registration = (By.XPATH, "//button[text()='Зарегистрироваться']")

    # страница входа
    login_page = (By.CLASS_NAME, 'Auth_login__3hAey')

    # Заголовок Вход
    title_login_page = (By.XPATH, "//h2[contains(text(),'Вход')]")

    # Ошибка не верного пароля
    alert_password_fail = (By.XPATH, '//p[contains(text(),"Некорректный пароль")]')

    # Кнопка войти в аккаунт на главной странице
    button_login_account = (By.XPATH, "//button[contains(text(),'Войти в аккаунт')]")

    # Кнопка входа в аккаунт
    button_login = (By.XPATH, '//button[contains(text(),"Войти")]')

    # Кнопка оформить заказ
    button_checkout = (By.XPATH, "//button[contains(text(),'Оформить заказ')]")

    # Кнопка перехода в личный кабинет
    button_personal_account = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]")

    # Кнопка Войти на странице регистрации
    button_login_registration_page = (By.XPATH, "//a[contains(text(),'Войти')]")

    # Кнопка восcтановить пароль на странице входа в аккаунт
    button_recovery_password = (By.XPATH, "//a[contains(text(),'Восстановить пароль')]")

    # Кнопка выхода из Личного кабинета
    button_exit = (By.XPATH, "//button[contains(text(),'Выход')]")

    # Секция Булки
    section_bun = (By.XPATH, "//span[text() = 'Булки']")

    # Секция соусов
    section_sauce = (By.XPATH, "//span[text() = 'Соусы']")

    # Секция Начинки
    section_filling = (By.XPATH, "//span[text() = 'Начинки']")

    # Флюоресцентная булка
    fluorescent_bun = "//p[contains(text(), 'Флюоресцентная булка')]"

    # Активная секция
    active_section = (By.XPATH, "//*[contains(@class, 'tab_tab_type_current')]")


class AppHeader:
    # Ссылка для входа в раздел конструктор
    link_constructor =(By.XPATH, "//p[contains(text(),'Конструктор')]")

    # Ссылка на логотип
    logo = (By.CLASS_NAME, 'AppHeader_header__logo__2D0X2')


class MainPage:

    # Заголовок на главной странице Соберите бургер
    title_main_page = (By.XPATH, "//h1[text() = 'Соберите бургер']")


    # Секция Начинки
    filling_element = (By.XPATH, "//span[text() = 'Начинки']")