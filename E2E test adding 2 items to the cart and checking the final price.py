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

# authorization
login_standard_user = "standard_user"
password_all = "secret_sauce"

user_name = driver.find_element(By.XPATH, "//input[@id='user-name']") # выбор поля логин
user_name.send_keys(login_standard_user) # ввод логина
print("input login")
user_password = driver.find_element(By.XPATH, "//input[@id='password']")# выбор поля пароль
user_password.send_keys(password_all) # ввод пароля
print("input password")
button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")# выбор кнопки login
button_login.click()
print("input button_login")

# info product_1
product_1 = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
value_product_1 = product_1.text # текстовое значение поля продукта 1
print(value_product_1)

price_product_1 = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div")
value_price_product_1 = price_product_1.text
print(value_price_product_1)

# info product_2
product_2 = driver.find_element(By.XPATH, "//a[@id='item_1_title_link']")
value_product_2 = product_2.text
print(value_product_2)

price_product_2 = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[3]/div[2]/div[2]/div")
value_price_product_2 = price_product_2.text
print(value_price_product_2)

#button add to cart for product_1
add_cart_product_1 = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
add_cart_product_1.click()
print("add_cart_product_1")

#button add to cart for product_2
add_cart_product_2 = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']")
add_cart_product_2.click()
print("add_cart_product_2")

#element cart
cart = driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']")
cart.click()
print("cart")

# info cart_product_1
cart_product_1 = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
value_cart_product_1 = cart_product_1.text
print("cart_product_1")

assert value_product_1 == value_cart_product_1
print("info cart_product_1 GOOD")

price_cart_product_1 = driver.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div")
value_price_cart_product_1 = price_cart_product_1.text
print("price_cart_product_1")

assert value_price_product_1 == value_price_cart_product_1
print("info cart_price_product_1 GOOD")

# info cart_product_2
cart_product_2 = driver.find_element(By.XPATH, "//a[@id='item_1_title_link']")
value_cart_product_2 = cart_product_2.text
print("cart_product_2")

assert value_product_2 == value_cart_product_2
print("info cart_product_2 GOOD")

price_cart_product_2 = driver.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[4]/div[2]/div[2]/div")
value_price_cart_product_2 = price_cart_product_2.text
print("price_cart_product_2")

assert value_price_product_2 == value_price_cart_product_2
print("info cart_price_product_2 GOOD")

#button checkout
checkout = driver.find_element(By.XPATH, "//button[@id='checkout']")
checkout.click()
print("click checkout")

# select user info
first_name = driver.find_element(By.XPATH, "//input[@id='first-name']")
first_name.send_keys("Alex")
print("input first_name")

last_name = driver.find_element(By.XPATH, "//input[@id='last-name']")
last_name.send_keys("Ivanov")
print("input last_name")

zip = driver.find_element(By.XPATH, "//input[@id='postal-code']")
zip.send_keys("1234")
print("input zip")

#button continue
button_continue = driver.find_element(By.XPATH, "//input[@id='continue']")
button_continue.click()
print("click button_continue")

# info finish_product_1
finish_product_1 = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
value_finish_product_1 = finish_product_1.text
print("finish_product_1")

assert value_product_1 == value_finish_product_1
print("info finish_product_1 GOOD")

price_finish_product_1 = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div")
value_price_finish_product_1 = price_finish_product_1.text
print("price_finish_product_1")

assert value_price_product_1 == value_price_finish_product_1
print("info finish_price_product_1 GOOD")

# info finish_product_2
finish_product_2 = driver.find_element(By.XPATH, "//a[@id='item_1_title_link']")
value_finish_product_2 = finish_product_2.text
print("finish_product_2")

assert value_product_2 == value_finish_product_2
print("info finish_product_2 GOOD")

price_finish_product_2 = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[4]/div[2]/div[2]/div")
value_price_finish_product_2 = price_finish_product_2.text
print("price_finish_product_2")

assert value_price_product_2 == value_price_finish_product_2
print("info finish_price_product_2 GOOD")

# item total price
summary_price = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[6]")
value_summary_price = summary_price.text
print("value_summary_price")
print(summary_price.text)
print(summary_price.text.split("$"))
massive = summary_price.text.split("$")
print(massive[1])


# replace $ from price product_1
cost_product_1 = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div")
value_cost_product_1 = cost_product_1.text
print("value_cost_product_1")
print(cost_product_1.text)
cost_product_1_number = float(cost_product_1.text.replace("$", ""))
print(cost_product_1_number)


# replace $ from price product_2
cost_product_2 = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[4]/div[2]/div[2]/div")
value_cost_product_2 = cost_product_2.text
print("value_cost_product_2")
print(cost_product_2.text)
cost_product_2_number = float(cost_product_2.text.replace("$", ""))
print(cost_product_2_number)



#checking final price
item_total = str(cost_product_1_number + cost_product_2_number)
print("item_total")
print(item_total)

assert massive[1] == item_total
print("checking final price GOOD")
