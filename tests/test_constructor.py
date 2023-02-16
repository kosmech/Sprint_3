from conftest import *

class TestConstructor:
    def test_constructor_section_bul(self, driver):

        # находим раздел "Начинки" и кликаем на него
        driver.find_element(*Locators.section_filling).click()

        # находим раздел "Булки" и кликаем на него
        driver.find_element(*Locators.section_bun).click()

        # Ждем появления элемента из раздела Булки
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//p[contains(text(), 'Флюоресцентная булка')]")))

        # Находим текст активного раздела и сравниваем
        assert driver.find_element(*Locators.active_section).text == 'Булки'
