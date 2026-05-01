import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, AuthPageLocators, RegisterPageLocators, ForgotPasswordPageLocators
from generators import generate_random_email, generate_random_password, generate_random_name

#Класс с тестами входа в аккаунт через: кнопку «Войти в аккаунт» на главной, кнопку «Личный кабинет» в шапке, ссылку «Войти» на форме регистрации и на на форме восстановления пароля
class TestLogin:

    #Вспомогательный метод: регистрируем нового пользователя и после регистрации остаемсяна странице входа
    def register_user(self, driver):

        driver.get("https://stellarburgers.education-services.ru/")  # открываем главную страницу
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click() # клик "Личный кабинет"

        wait = WebDriverWait(driver, 5)

        wait.until(EC.element_to_be_clickable(AuthPageLocators.REGISTER_LINK)).click()    # переходим к регистрации
        wait.until(EC.visibility_of_element_located(RegisterPageLocators.NAME_INPUT))     # дождались загрузки страницы регистрации
        
        name = generate_random_name()                                                             
        email = generate_random_email()                                                           
        password = generate_random_password(6)                                                    
        
        driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys(name)                     
        driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(email)                   
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(password)             
        driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()                        
        
        wait.until(EC.visibility_of_element_located(AuthPageLocators.LOGIN_BUTTON)) # ждём кнопку "Войти" (успех регистрации)
        return email, password  # возвращаем данные для входа
    

    #Проверяем вход по кнопке «Войти в аккаунт» на главной странице
    def test_login_by_main_button(self, driver):

        email, password = self.register_user(driver)             

        driver.get("https://stellarburgers.education-services.ru/")  # открываем главную страницу
        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()  # клик "Войти в аккаунт" на главной

        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located(AuthPageLocators.EMAIL_INPUT))  # ждём поле email на форме входа

        driver.find_element(*AuthPageLocators.EMAIL_INPUT).send_keys(email)   # вводим email
        driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(password)    # вводим пароль
        driver.find_element(*AuthPageLocators.LOGIN_BUTTON).click()   # нажимаем "Войти"

        wait.until(EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON))   # ждём кнопку "Оформить заказ"
        assert driver.find_element(*MainPageLocators.ORDER_BUTTON).is_displayed()     # проверяем, что вход выполнен
    

    #Проверяем вход через кнопку «Личный кабинет» в шапке сайта
    def test_login_by_personal_account_button(self, driver):

        email, password = self.register_user(driver)                    

        driver.get("https://stellarburgers.education-services.ru/")   # открываем главную страницу
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()   # клик "Личный кабинет" в шапке

        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located(AuthPageLocators.EMAIL_INPUT))            

        driver.find_element(*AuthPageLocators.EMAIL_INPUT).send_keys(email)                     
        driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(password)               
        driver.find_element(*AuthPageLocators.LOGIN_BUTTON).click()           

        wait.until(EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON))  # ждём кнопку "Оформить заказ"
        assert driver.find_element(*MainPageLocators.ORDER_BUTTON).is_displayed()   # проверяем, что вход выполнен
    

    #Проверяем вход через ссылку «Войти» на форме регистрации
    def test_login_by_register_form(self, driver):

        email, password = self.register_user(driver)      

        driver.get("https://stellarburgers.education-services.ru/")    # открываем главную страницу
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()  # клик "Личный кабинет"

        wait = WebDriverWait(driver, 5)
        wait.until(EC.element_to_be_clickable(AuthPageLocators.REGISTER_LINK)).click()  # переходим к регистрации
        wait.until(EC.visibility_of_element_located(RegisterPageLocators.NAME_INPUT))   

        driver.find_element(*RegisterPageLocators.LOGIN_LINK).click()     # на странице регистрации кликаем "Войти"
        wait.until(EC.visibility_of_element_located(AuthPageLocators.EMAIL_INPUT))    

        driver.find_element(*AuthPageLocators.EMAIL_INPUT).send_keys(email)                     
        driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(password)               
        driver.find_element(*AuthPageLocators.LOGIN_BUTTON).click()    # нажимаем "Войти"

        wait.until(EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON))  # ждём кнопку "Оформить заказ"
        assert driver.find_element(*MainPageLocators.ORDER_BUTTON).is_displayed()  # проверяем, что вход выполнен
    

    #Проверяем вход через ссылку «Войти» на форме восстановления пароля
    def test_login_by_forgot_password_form(self, driver):

        email, password = self.register_user(driver)        # регистрируемся

        driver.get("https://stellarburgers.education-services.ru/")    # открываем главную страницу
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()   # клик "Личный кабинет"

        wait = WebDriverWait(driver, 5)
        wait.until(EC.element_to_be_clickable(AuthPageLocators.FORGOT_PASSWORD_LINK)).click()  # переходим к восстановлению пароля
        wait.until(EC.visibility_of_element_located(ForgotPasswordPageLocators.LOGIN_LINK))   # ждём ссылку "Войти" на странице восстановления

        driver.find_element(*ForgotPasswordPageLocators.LOGIN_LINK).click()    # кликаем "Войти"
        wait.until(EC.visibility_of_element_located(AuthPageLocators.EMAIL_INPUT))         

        driver.find_element(*AuthPageLocators.EMAIL_INPUT).send_keys(email)                     
        driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(password)               
        driver.find_element(*AuthPageLocators.LOGIN_BUTTON).click()              
                       
        wait.until(EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON))            
        assert driver.find_element(*MainPageLocators.ORDER_BUTTON).is_displayed() # проверяем, что вход выполнен