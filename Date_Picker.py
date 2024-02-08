import time

from selenium import webdriver #импортируем модуль вебдрайвер из библиотеки селениум, который позволяет нам управлять веб-браузером
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service # импортируем модуль сёрвис из библиотеки селениум


options = webdriver.ChromeOptions() # создаем объект, который позволяет настраиваить параметры запуска браузера Хром
options.add_experimental_option("detach", True) # добавляем опцию detach со значением True. Опция позволяет отключить автоматическое закрытие браузера после выполнения скрипта
g = Service() # создаем объект g класса service для настройки сервиса ХромДрайвер
driver = webdriver.Chrome(options=options, service=g) # создаем экзепляр браузера Хром, используя опции из объекта options и сервис из объекта g. Настраиваем браузер с опцией detach и сервисом ХромДрайвер
base_url = 'https://demoqa.com/date-picker'
driver.get(base_url)
# driver.maximize_window()


# Date_Picker

# new_date = driver.find_element(By.XPATH, "//input[@id='datePickerMonthYearInput']")

# product_1 = driver.find_element(By.XPATH, "//input[@id='datePickerMonthYearInput']")
# new_date.click()
# time.sleep(5)
