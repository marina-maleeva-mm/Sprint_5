from random import randint
from selenium import webdriver
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import MainPageLocators, AuthPageLocators, RegistrationPageLocators
from urls import Urls


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()



@pytest.fixture
def create_user(driver):
    name = 'Марина'
    email = f'marina_maleeva_46_{randint(1000, 999999)}@mail.ru'
    password = '12345Qwerty'

    driver.get(Urls.REGISTRATION_PAGE_URL)
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(RegistrationPageLocators.registration_button)
    )

    driver.find_element(*RegistrationPageLocators.name_input).send_keys(name)
    driver.find_element(*RegistrationPageLocators.email_input).send_keys(email)
    driver.find_element(*RegistrationPageLocators.password_input).send_keys(password)
    driver.find_element(*RegistrationPageLocators.registration_button).click()

    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(AuthPageLocators.login_account_button)
    )

    return email, password


@pytest.fixture
def get_login_driver(driver, create_user):
    email, password = create_user

    driver.get(Urls.MAIN_PAGE_URL)
    driver.find_element(*MainPageLocators.personal_account_button).click()
    driver.find_element(*AuthPageLocators.email_input).send_keys(email)
    driver.find_element(*AuthPageLocators.password_input).send_keys(password)
    driver.find_element(*AuthPageLocators.login_account_button).click()

    return driver