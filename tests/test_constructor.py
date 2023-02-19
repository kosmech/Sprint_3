from conftest import *

class TestConstructor:
    def test_constructor_section_bul(self, driver):

        # находим раздел "Начинки" и кликаем на него
        driver.find_element(*Locators.section_filling).click()

        # находим раздел "Булки" и кликаем на него
        driver.find_element(*Locators.section_bun).click()

        # делаем прокрутку до заголовка "Булки"
        element_bul = driver.find_element(*Locators.title_bul)
        driver.execute_script("arguments[0].scrollIntoView();", element_bul)

        # Находим текст активного раздела и сравниваем
        assert driver.find_element(*Locators.active_section).text == 'Булки'

    def test_constructor_section_sauce(self, driver):

        # находим раздел "Начинки" и кликаем на него
        driver.find_element(*Locators.section_filling).click()

        # находим раздел "Соусы" и кликаем на него
        driver.find_element(*Locators.section_sauce).click()

        # делаем прокрутку до заголовка "Соусы"
        element_sauce = driver.find_element(*Locators.title_sauce)
        driver.execute_script("arguments[0].scrollIntoView();", element_sauce)

        # Находим текст активного раздела и сравниваем
        assert driver.find_element(*Locators.active_section).text == 'Соусы'

    def test_constructor_section_filling(self, driver):

        # находим раздел "Начинки" и кликаем на него
        driver.find_element(*Locators.section_filling).click()

        # делаем прокрутку до заголовка "Начинки"
        element_filling = driver.find_element(*Locators.title_filling)
        driver.execute_script("arguments[0].scrollIntoView();", element_filling)

        # Находим текст активного раздела и сравниваем
        assert driver.find_element(*Locators.active_section).text == 'Начинки'