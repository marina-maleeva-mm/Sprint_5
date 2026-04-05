from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import MainPageLocators
from urls import Urls


class TestConstructorPage:

    #Проверка перехода к разделу 'Булки'
    def test_open_bun_section_success(self, driver):
        driver.get(Urls.MAIN_PAGE_URL)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(MainPageLocators.toppings_button))

        driver.find_element(*MainPageLocators.sauces_button).click()
        driver.find_element(*MainPageLocators.buns_button).click()

        assert driver.find_element(*MainPageLocators.buns).is_displayed()


    # Проверка перехода к разделу 'Соусы'
    def test_transition_to_sauces_success(self, driver):
        driver.get(Urls.MAIN_PAGE_URL)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(MainPageLocators.sauces_button))

        driver.find_element(*MainPageLocators.sauces_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(MainPageLocators.sauces))

        assert driver.find_element(*MainPageLocators.sauces).is_displayed()


    # Проверка перехода к разделу 'Начинки'
    def test_open_ingridients_section_success(self, driver):
        driver.get(Urls.MAIN_PAGE_URL)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(MainPageLocators.toppings_button))

        driver.find_element(*MainPageLocators.toppings_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(MainPageLocators.toppings))

        assert driver.find_element(*MainPageLocators.toppings).is_displayed()