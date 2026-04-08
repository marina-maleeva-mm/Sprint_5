from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import MainPageLocators, AuthPageLocators, RegistrationPageLocators, RecoverPageLocators
from urls import Urls


class TestLoginPage:

    #Вход в личный кабинет через кнопку 'Войти в аккаунт' на главной странице
    def test_login_from_main_page_button_success(self, driver, create_user):
        email, password = create_user

        driver.get(Urls.MAIN_PAGE_URL)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(MainPageLocators.login_account_button))

        driver.find_element(*MainPageLocators.login_account_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(AuthPageLocators.login_account_button))

        driver.find_element(*AuthPageLocators.email_input).send_keys(email)
        driver.find_element(*AuthPageLocators.password_input).send_keys(password)
        driver.find_element(*AuthPageLocators.login_account_button).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(MainPageLocators.place_order_button))
        
        assert driver.current_url == Urls.MAIN_PAGE_URL
        assert driver.find_element(*MainPageLocators.place_order_button).is_displayed()

    
    #Вход в личный кабинет через кнопку 'Личный кабинет' на главной странице
    def test_login_from_personal_account_button_success(self, driver, create_user):
        email, password = create_user

        driver.get(Urls.MAIN_PAGE_URL)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(MainPageLocators.personal_account_button))

        driver.find_element(*MainPageLocators.personal_account_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(AuthPageLocators.login_account_button))

        driver.find_element(*AuthPageLocators.email_input).send_keys(email)
        driver.find_element(*AuthPageLocators.password_input).send_keys(password)
        driver.find_element(*AuthPageLocators.login_account_button).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(MainPageLocators.place_order_button))

        assert driver.current_url == Urls.MAIN_PAGE_URL
        assert driver.find_element(*MainPageLocators.place_order_button).is_displayed()


    #Вход в личный кабинет через форму регистрации
    def test_login_from_registration_page_button_success(self, driver, create_user):
        email, password = create_user

        driver.get(Urls.REGISTRATION_PAGE_URL)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(RegistrationPageLocators.login_account_button))

        driver.find_element(*RegistrationPageLocators.login_account_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(AuthPageLocators.login_account_button))

        driver.find_element(*AuthPageLocators.email_input).send_keys(email)
        driver.find_element(*AuthPageLocators.password_input).send_keys(password)
        driver.find_element(*AuthPageLocators.login_account_button).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(MainPageLocators.place_order_button))

        assert driver.current_url == Urls.MAIN_PAGE_URL
        assert driver.find_element(*MainPageLocators.place_order_button).is_displayed()


    #Вход в личный кабинет через форму восстановления пароля
    def test_login_in_recover_form_success(self, driver, create_user):
        email, password = create_user

        driver.get(Urls.RECOVER_PAGE_URL)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(RecoverPageLocators.login_account_button))

        driver.find_element(*RecoverPageLocators.login_account_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(AuthPageLocators.login_account_button))

        driver.find_element(*AuthPageLocators.email_input).send_keys(email)
        driver.find_element(*AuthPageLocators.password_input).send_keys(password)
        driver.find_element(*AuthPageLocators.login_account_button).click()
        
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(MainPageLocators.place_order_button))
        
        assert driver.current_url == Urls.MAIN_PAGE_URL
        assert driver.find_element(*MainPageLocators.place_order_button).is_displayed()
    