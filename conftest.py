import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Написала фикстуру driver (для создания и закрытия драйвера браузера – она будет автоматически использоваться в каждом тесте)

@pytest.fixture
def driver():

    # Настройки браузера Chrome
    options = Options()
    options.add_argument("--window-size=1920,1080")  # Устанавила размер окна
    
    # Создала экземпляр драйвера (что бы открылось новое окно браузера)
    driver = webdriver.Chrome(options=options)
    
    # Передала драйвер в тест (yield вместо return, чтобы после теста выполнить код)
    yield driver
    
    # После завершения теста закрываем браузер
    driver.quit()