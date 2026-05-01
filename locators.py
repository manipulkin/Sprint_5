from selenium.webdriver.common.by import By

#Локаторы 
class MainPageLocators:
    
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']") # Кнопка «Войти в аккаунт» на главной странице   
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']") # Кнопка «Оформить заказ» — появляется после успешного входа
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//a[contains(@href,'/account')]") # Кнопка «Личный кабинет» в шапке сайта
    LOGO = (By.XPATH, "//header//a[@href='/']") # Логотип Stellar Burgers в шапке (ведёт на главную)
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']/..") # Ссылка «Конструктор» в шапке сайта
    BUNS_SECTION = (By.XPATH, "//div[span[text()='Булки']]") # Вкладка «Булки» в конструкторе
    SAUCES_SECTION = (By.XPATH, "//div[span[text()='Соусы']]") # Вкладка «Соусы» в конструкторе
    FILLINGS_SECTION = (By.XPATH, "//div[span[text()='Начинки']]") # Вкладка «Начинки» в конструкторе
    ACTIVE_SECTION_TITLE = (By.XPATH, "//div[contains(@class,'tab_tab_type_current')]//span") # Активная вкладка конструктора
 

#Локаторы страницы входа
class AuthPageLocators:

    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input") # Поле «Email» на форме входа
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")  #Поле «Пароль» на форме входа
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']") # Кнопка «Войти» на форме входа
    REGISTER_LINK = (By.XPATH, "//a[@href='/register']") # Ссылка «Зарегистрироваться» на форме входа
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[@href='/forgot-password']") # Ссылка «Восстановить пароль» на форме входа


#Локаторы страницы регистрации
class RegisterPageLocators:

    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input") # Поле «Имя» на форме регистрации
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input") # Поле «Email» на форме регистрации
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input") # Поле «Пароль» на форме регистрации
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']") # Кнопка «Зарегистрироваться»
    ERROR_MESSAGE_INVALID_PASSWORD = (By.XPATH, "//p[contains(@class,'input__error') and text()='Некорректный пароль']") # Сообщение об ошибке 
    LOGIN_LINK = (By.XPATH, "//a[@href='/login']") # Ссылка «Войти» на форме регистрации


#Локаторы личного кабинета
class PersonalAccountPageLocators:

    EXIT_BUTTON = (By.XPATH, "//button[text()='Выход']") # Кнопка «Выход» в личном кабинете


#Локаторы страницы восстановления пароля
class ForgotPasswordPageLocators:

    LOGIN_LINK = (By.XPATH, "//a[@href='/login']") # Ссылка «Войти» на форме восстановления пароля