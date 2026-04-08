from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import RegistrationPageLocators, AuthPageLocators
from data import Person, RandomData
from urls import Urls



class TestRegistrationPage:
    
    # Проверка регистрации пользователя
    def test_registration_success(self, driver):
        driver.get(Urls.REGISTRATION_PAGE_URL)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(RegistrationPageLocators.registration_button))

        driver.find_element(*RegistrationPageLocators.name_input).send_keys(RandomData.user_name)
        driver.find_element(*RegistrationPageLocators.email_input).send_keys(RandomData.email)
        driver.find_element(*RegistrationPageLocators.password_input).send_keys(RandomData.password)

        driver.find_element(*RegistrationPageLocators.registration_button).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(AuthPageLocators.login_account_button))

        assert driver.current_url == Urls.AUTH_PAGE_URL
        assert driver.find_element(*AuthPageLocators.login_account_button).is_displayed()


    # Проверка регистрации пользователя с некорректным паролем (менее 6 символов)
    def test_registration_incorrect_password_check_error(self, driver):
        driver.get(Urls.REGISTRATION_PAGE_URL)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(RegistrationPageLocators.registration_button))

        driver.find_element(*RegistrationPageLocators.name_input).send_keys(RandomData.user_name)
        driver.find_element(*RegistrationPageLocators.email_input).send_keys(RandomData.email)
        driver.find_element(*RegistrationPageLocators.password_input).send_keys('12345')

        driver.find_element(*RegistrationPageLocators.registration_button).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(RegistrationPageLocators.error_message_incorrect_password))
        error = driver.find_element(*RegistrationPageLocators.error_message_incorrect_password).text

        assert error == 'Некорректный пароль'
        assert driver.current_url == Urls.REGISTRATION_PAGE_URL