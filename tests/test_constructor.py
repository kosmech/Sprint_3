from conftest import *

class TestConstructor:
    def test_constructor_section_bul(self, driver):

        # находим раздел "Начинки" и кликаем на него
        driver.find_element(*Locators.section_filling).click()

        # находим раздел "Булки" и кликаем на него
        driver.find_element(*Locators.section_bun).click()

        # Находим текст активного раздела и сравниваем
        assert driver.find_element(*Locators.active_section).text == 'Булки'

    def test_constructor_section_sauce(self, driver):

        # находим раздел "Соусы" и кликаем на него
        driver.find_element(*Locators.section_sauce).click()

        # Находим текст активного раздела и сравниваем
        assert driver.find_element(*Locators.active_section).text == 'Соусы'

    def test_constructor_section_filling(self, driver):

        # находим раздел "Начинки" и кликаем на него
        driver.find_element(*Locators.section_filling).click()

        # Находим текст активного раздела и сравниваем
        assert driver.find_element(*Locators.active_section).text == 'Начинки'

