import random
import string

# Генерируем email для регистрации, в котором 8 случайных символов (буквы и цифры) + '@testdomain.ru'
def generate_random_email():
        
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f"{random_string}@testdomain.ru"

# Генерируем пароль заданной длины (по умолчанию 6 символов), при этом используем буквы (верхний и нижний регистр) и цифры.
def generate_random_password(min_length=6):
       
    return ''.join(random.choices(string.ascii_letters + string.digits, k=min_length))

# Генерируем случайное имя пользователя (только буквы, 8 символов).
def generate_random_name():
       
    return ''.join(random.choices(string.ascii_letters, k=8))