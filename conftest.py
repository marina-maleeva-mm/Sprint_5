from selenium import webdriver
import pytest
from locators import MainPageLocators, AuthPageLocators
from urls import Urls
from data import Person


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()



@pytest.fixture
def get_login_driver(driver):
    driver.get(Urls.MAIN_PAGE_URL)
    driver.find_element(*MainPageLocators.personal_account_button).click()
    driver.find_element(*AuthPageLocators.email_input).send_keys(Person.email)
    driver.find_element(*AuthPageLocators.password_input).send_keys(Person.password)
    driver.find_element(*AuthPageLocators.login_account_button).click()
    
    return driver