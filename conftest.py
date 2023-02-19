import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from locators import *

url = 'https://stellarburgers.nomoreparties.site/'

@pytest.fixture()
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--window-size=1280,720')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    yield driver
    driver.quit()