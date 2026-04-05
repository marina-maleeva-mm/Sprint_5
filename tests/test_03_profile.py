from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import MainPageLocators, PersonalAreaLocators, AuthPageLocators
from urls import Urls


class TestPersonalArea:
    
    # Проверка перехода в личный кабинет с главной страницы по клику на 'Личный кабинет'
    def test_open_personal_account_from_main_page_success(self, get_login_driver):
        driver = get_login_driver
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(MainPageLocators.personal_account_button))

        driver.find_element(*MainPageLocators.personal_account_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(PersonalAreaLocators.profile_form))

        assert driver.current_url == Urls.PROFILE_PAGE_URL
        assert driver.find_element(*PersonalAreaLocators.profile_form).is_displayed()


    # Проверка перехода из личного кабинета в конструктор по клику на 'Конструктор'
    def test_open_constructor_from_personal_account_by_constructor_button_success(self, get_login_driver):
        driver = get_login_driver
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(MainPageLocators.personal_account_button))

        driver.find_element(*MainPageLocators.personal_account_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(PersonalAreaLocators.constructor_button))

        driver.find_element(*PersonalAreaLocators.constructor_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(MainPageLocators.place_order_button))

        assert driver.current_url == Urls.MAIN_PAGE_URL
        assert driver.find_element(*MainPageLocators.place_order_button).is_displayed()


    # Проверка перехода из личного кабинета в конструктор по клику на 'Логотип Stellar Burger'
    def test_open_constructor_from_personal_account_by_logo_success(self, get_login_driver):
        driver = get_login_driver
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(MainPageLocators.personal_account_button))

        driver.find_element(*MainPageLocators.personal_account_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(PersonalAreaLocators.logo_button))

        driver.find_element(*PersonalAreaLocators.logo_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(MainPageLocators.place_order_button))

        assert driver.current_url == Urls.MAIN_PAGE_URL
        assert driver.find_element(*MainPageLocators.place_order_button).is_displayed()


    # Проверка выхода из личного кабинета по клику на 'Выйти'
    def test_logout_from_personal_account_success(self, get_login_driver):
        driver = get_login_driver
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(MainPageLocators.personal_account_button))

        driver.find_element(*MainPageLocators.personal_account_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(PersonalAreaLocators.exit_button))

        driver.find_element(*PersonalAreaLocators.exit_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.url_contains('login'))

        assert driver.current_url == Urls.AUTH_PAGE_URL
        assert driver.find_element(*AuthPageLocators.login_account_button).is_displayed()