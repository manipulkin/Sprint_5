import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, AuthPageLocators, RegisterPageLocators, PersonalAccountPageLocators
from generators import generate_random_email, generate_random_password, generate_random_name

#Тесты переходов (личный кабинет)
class TestPersonalAccount:

    #Вспомогательный метод: регистрируем нового пользователя, который авторизован и находится на главной страницк 
    def register_and_login(self, driver):

        driver.get("https://stellarburgers.education-services.ru/")  # открываем главную страницу
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click() # клик "Личный кабинет"
        wait = WebDriverWait(driver, 5)
        wait.until(EC.element_to_be_clickable(AuthPageLocators.REGISTER_LINK)).click() # переходим к регистрации
        wait.until(EC.visibility_of_element_located(RegisterPageLocators.NAME_INPUT))  # дождались загрузки страницы регистрации
        
        name = generate_random_name()                                                             
        email = generate_random_email()                                                           
        password = generate_random_password(6)                                                    
        
        driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys(name)   # заполняем имя
        driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(email)  # заполняем email
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(password)  # заполняем пароль
        driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()  # нажимаем "Зарегистрироваться"
        
        wait.until(EC.visibility_of_element_located(AuthPageLocators.LOGIN_BUTTON)) # ждём кнопку "Войти" (успех регистрации)
        driver.find_element(*AuthPageLocators.EMAIL_INPUT).send_keys(email) # вводим email
        driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(password)   # вводим пароль
        driver.find_element(*AuthPageLocators.LOGIN_BUTTON).click()     # нажимаем "Войти"
        wait.until(EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)) # ждём кнопку "Оформить заказ"
    

    #Проверяем пееход в личный кабинет по клику на «Личный кабинет»
    def test_go_to_personal_account(self, driver):
  
        self.register_and_login(driver)      # регистрируем и входим

        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()  # клик "Личный кабинет"
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located(PersonalAccountPageLocators.EXIT_BUTTON))    # ждём кнопку "Выход"

        assert driver.find_element(*PersonalAccountPageLocators.EXIT_BUTTON).is_displayed()  # проверяем, что открылся личный кабинет
    

    #Проверяем переход из личного кабинета в конструктор по кнопке «Конструктор»
    def test_go_from_personal_account_to_constructor_by_button(self, driver):

        self.register_and_login(driver)    # регистрируем и входим

        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()  # клик "Личный кабинет"
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located(PersonalAccountPageLocators.EXIT_BUTTON)) # ждём кнопку "Выход"

        driver.find_element(*MainPageLocators.CONSTRUCTOR_BUTTON).click()    # клик "Конструктор" в шапке
        wait.until(EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)) # ждём кнопку "Оформить заказ"
        assert driver.find_element(*MainPageLocators.ORDER_BUTTON).is_displayed()   # проверяем, что вернулись на главную
    

    #Проверяем переход из личного кабинета в конструктор по логотипу Stellar Burgers
    def test_go_from_personal_account_to_constructor_by_logo(self, driver):

        self.register_and_login(driver)      

        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()  # клик "Личный кабинет"
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located(PersonalAccountPageLocators.EXIT_BUTTON))  

        driver.find_element(*MainPageLocators.LOGO).click()    # клик по логотипу
        wait.until(EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON))    
        assert driver.find_element(*MainPageLocators.ORDER_BUTTON).is_displayed()   # проверяем, что вернулись на главную
    

    #Проверяем выход из аккаунта по кнопке «Выйти» в личном кабинете
    def test_logout(self, driver):

        self.register_and_login(driver)                            

        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()     
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located(PersonalAccountPageLocators.EXIT_BUTTON))    # ждём кнопку "Выход"

        driver.find_element(*PersonalAccountPageLocators.EXIT_BUTTON).click()  # нажимаем "Выход"
        wait.until(EC.visibility_of_element_located(AuthPageLocators.LOGIN_BUTTON))  # ждём кнопку "Войти" на странице входа
        assert driver.find_element(*AuthPageLocators.LOGIN_BUTTON).is_displayed()    # проверяем, что вышли из аккаунта