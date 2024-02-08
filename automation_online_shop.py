import time

from selenium import webdriver #импортируем модуль вебдрайвер из библиотеки селениум, который позволяет нам управлять веб-браузером
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service # импортируем модуль сёрвис из библиотеки селениум



options = webdriver.ChromeOptions() # создаем объект, который позволяет настраиваить параметры запуска браузера Хром
options.add_experimental_option("detach", True) # добавляем опцию detach со значением True. Опция позволяет отключить автоматическое закрытие браузера после выполнения скрипта
g = Service() # создаем объект g класса service для настройки сервиса ХромДрайвер
driver = webdriver.Chrome(options=options, service=g) # создаем экзепляр браузера Хром, используя опции из объекта options и сервис из объекта g. Настраиваем браузер с опцией detach и сервисом ХромДрайвер
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

user_name = driver.find_element(By.ID, "user-name") # выбор поля логин
user_name.send_keys("standard_user") # ввод логина
time.sleep(5)
user_name.clear()
# user_password = driver.find_element(By.ID, "password") # выбор поля пароль
# user_password.send_keys("secret_sauce") # ввод пароля
# button_login = driver.find_element(By.ID, "login-button") # выбор кнопки login
# time.sleep(5)
# button_login.click() # нажатие кнопки


