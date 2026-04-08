from selenium.webdriver.common.by import By

# Главная страница
class MainPageLocators:
    constructor_button = (By.XPATH, ".//p[text() = 'Конструктор']") # Кнопка Конструктор
    logo_button = (By.XPATH, ".//div[@class = 'AppHeader_header__logo__2D0X2']") # Кнопка главной страницы сайта (Логотип)
    personal_account_button = (By.XPATH, ".//p[text() = 'Личный Кабинет']") # Кнопка личного кабинета
    login_account_button = (By.XPATH, ".//button[text() = 'Войти в аккаунт']") # Кнопка войти в аккаунт
    buns_button = (By.XPATH, ".//span[text() = 'Булки']/parent::div") # Кнопка переключения на Булки
    sauces_button = (By.XPATH, ".//span[text() = 'Соусы']/parent::div") # Кнопка переключения на Соусы
    toppings_button = (By.XPATH, ".//span[text() = 'Начинки']/parent::div") # Кнопка переключения на Начинки
    place_order_button = (By.XPATH, ".//button[text() = 'Оформить заказ']") # Кнопка Оформить заказ
    sauces = (By.XPATH, ".//h2[text() = 'Соусы']") # Текст Соусы на главной странице
    buns = (By.XPATH, ".//h2[text() = 'Булки']") # Текст Булки на главной странице
    toppings = (By.XPATH, ".//h2[text() = 'Начинки']") # Текст Начинки на главной странице


# Форма авторизации
class AuthPageLocators:
    email_input = (By.XPATH, ".//input[@name = 'name']") # Поле ввода email
    password_input = (By.XPATH, ".//input[@name = 'Пароль']") # Поле ввода пароля
    login_account_button = (By.XPATH, "//button[text() = 'Войти']") # Кнопка войти
    registration_button = (By.XPATH, "//a[text() = 'Зарегистрироваться']") # Кнопка Зарегистрироваться
    recover_button = (By.XPATH, "//a[text() = 'Восстановить пароль']") # Кнопка Восстановить пароль
    

# Форма регистрации
class RegistrationPageLocators:
    name_input = (By.XPATH, "(.//input[@name = 'name'])[1]") # Поле ввода имени
    email_input = (By.XPATH, "(.//input[@name = 'name'])[2]") # Поле ввода email
    password_input = (By.XPATH, ".//input[@name = 'Пароль']") # Поле ввода пароля
    registration_button = (By.XPATH, ".//button[text() = 'Зарегистрироваться']") # Кнопка зерегистрироваться
    login_account_button = (By.XPATH, ".//a[text() = 'Войти']") # Кнопка войти
    error_message_incorrect_password = (By.XPATH, ".//p[text() = 'Некорректный пароль']") # Ошибка при вводе некорректного пароля


# Форма восстановления пароля
class RecoverPageLocators:
    email_input = (By.XPATH, ".//label[text() = 'Email']") # Поле ввода email
    recover_button = (By.XPATH, ".//button[text() = 'Восстановить']") # Кнопка Восстановить
    login_account_button = (By.XPATH, ".//a[text() = 'Войти']") # Кнопка Войти
    constructor_button = (By.XPATH, ".//p[text() = 'Конструктор']") # Кнопка Конструктор


# Форма личного кабинета
class PersonalAreaLocators:
    profile_form = (By.XPATH, ".//div[@class = 'Account_account__vgk_w']") # Форма личного кабинета
    profile_button = (By.XPATH, ".//a[text() = 'Профиль']") # Кнопка профиль
    order_history_button = (By.XPATH, ".//a[text() = 'История заказов']") # Кнопка история заказов
    exit_button = (By.XPATH, ".//button[text() = 'Выход']") # Кнопка выход
    save_button = (By.XPATH, ".//button[text() = 'Сохранить']") # Кнопка сохранить
    cancel_button = (By.XPATH, ".//button[text() = 'Отмена']") # Кнопка отмена
    constructor_button = (By.XPATH, ".//p[text() = 'Конструктор']") # Кнопка Конструктор
    logo_button = (By.XPATH, ".//div[@class = 'AppHeader_header__logo__2D0X2']") # Кнопка главной страницы сайта (Логотип)