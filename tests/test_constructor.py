import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators

#Тесты переключения между разделами конструктора бургеров: булки, соусы, начинки 
class TestConstructor:

    #Проверяем переход к разделу «Булки» в конструкторе
    def test_switch_to_buns_section(self, driver):

        driver.get("https://stellarburgers.education-services.ru/")   # открываем главную страницу
        driver.find_element(*MainPageLocators.SAUCES_SECTION).click()   # клик на вкладку «Соусы», что бы уйти с вкладки «Булки»

        WebDriverWait(driver, 3)                   

        driver.find_element(*MainPageLocators.BUNS_SECTION).click()   # клик на вкладку «Булки»
        active_tab = driver.find_element(*MainPageLocators.ACTIVE_SECTION_TITLE)  # находим активную вкладку
        assert "Булки" in active_tab.text   # проверяем, что активна «Булки»
    

    #Проверяем переход к разделу «Соусы»
    def test_switch_to_sauces_section(self, driver):

        driver.get("https://stellarburgers.education-services.ru/")  # открываем главную страницу
        driver.find_element(*MainPageLocators.SAUCES_SECTION).click()   # клик на вкладку «Соусы»

        active_tab = driver.find_element(*MainPageLocators.ACTIVE_SECTION_TITLE)  # находим активную вкладку
        assert "Соусы" in active_tab.text   # проверяем, что активна «Соусы»
    

    #Проверяем переход к разделу «Начинки»
    def test_switch_to_fillings_section(self, driver):

        driver.get("https://stellarburgers.education-services.ru/")  # открываем главную страницу
        driver.find_element(*MainPageLocators.FILLINGS_SECTION).click()   # клик на вкладку «Начинки»
        
        active_tab = driver.find_element(*MainPageLocators.ACTIVE_SECTION_TITLE) # находим активную вкладку
        assert "Начинки" in active_tab.text  # проверяем, что активна «Начинки»