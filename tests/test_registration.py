import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, AuthPageLocators, RegisterPageLocators
from generators import generate_random_email, generate_random_password, generate_random_name

#Проверяет успешную регистрацию и ошибку при коротком пароле
class TestRegistration:

    #Проверяем успешную регистрацию с валидными данными
    def test_successful_registration(self, driver):

        driver.get("https://stellarburgers.education-services.ru/")  # открываем главную страницу
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()   # кликакем "Личный кабинет"
        wait = WebDriverWait(driver, 5)
        wait.until(EC.element_to_be_clickable(AuthPageLocators.REGISTER_LINK)).click()  # переходим к регистрации
        wait.until(EC.visibility_of_element_located(RegisterPageLocators.NAME_INPUT))  # дождались загрузки страницы регистрации
        
        name = generate_random_name()      # генерируем имя
        email = generate_random_email()          # генерируем email
        password = generate_random_password(6)   # генерируем пароль (6 символов)
        
        driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys(name)   # заполняем имя
        driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(email)      # заполняем email
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(password)  # заполняем пароль
        driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()  # нажимаем "Зарегистрироваться"
        
        wait.until(EC.visibility_of_element_located(AuthPageLocators.LOGIN_BUTTON))  # ждём кнопку "Войти" (успех регистрации)
        assert driver.find_element(*AuthPageLocators.LOGIN_BUTTON).is_displayed()  # проверяем, что кнопка "Войти" видна
    

    #Проверяем ошибку при регистрации с паролем короче 6 символов
    def test_registration_error_invalid_password(self, driver):

        driver.get("https://stellarburgers.education-services.ru/")  # открываем главную страницу
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()     # клик "Личный кабинет"
        wait = WebDriverWait(driver, 5)
        wait.until(EC.element_to_be_clickable(AuthPageLocators.REGISTER_LINK)).click()   # переходим к регистрации
        wait.until(EC.visibility_of_element_located(RegisterPageLocators.NAME_INPUT))    # дождались загрузки страницы регистрации
        
        name = generate_random_name()    # генерируем имя
        email = generate_random_email()     # генерируем email
        password = generate_random_password(5)     # генерируем пароль (5 символов – некорректный)
        
        driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys(name)   # заполняем имя
        driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(email)     # заполняем email
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(password)    # заполняем пароль
        driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()        # нажимаем "Зарегистрироваться"
        
        error = wait.until(EC.visibility_of_element_located(RegisterPageLocators.ERROR_MESSAGE_INVALID_PASSWORD))  # ждём сообщение об ошибке
        assert error.is_displayed()                       # проверяем, что сообщение видно
        assert "Некорректный пароль" in error.text        # проверяем текст ошибки