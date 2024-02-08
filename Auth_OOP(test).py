<<<<<<< HEAD
import time


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from LoginPage import LoginPage

accepted_usernames = ["standard_user", "locked_out_user", "problem_user", "performance_glitch_user"] # создаем список имен

for usernames in accepted_usernames:       # создаем цикл по списку имен
    print(usernames)







class Test_1():

    def test_select_product(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        g = Service('C:\\Users\\user\\PycharmProjects\\resource\\chromedriver.exe')
        driver = webdriver.Chrome(options=options, service=g)
        base_url = 'https://www.saucedemo.com/'
        driver.get(base_url)
        driver.maximize_window()
        time.sleep(5)

        print("Start Test")

        login_standard_user = "standard_user"
        password_all = "secret_sauce"

        login = LoginPage(driver) # создадим переменную, которая будет является экземпляром класса LoginPage
        login.authorization(login_standard_user, password_all)




        select_product = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,  "//button[@id='add-to-cart-sauce-labs-backpack']")))
        select_product.click()
        print("click select product")

        enter_shopping_cart = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,  "//div[@id='shopping_cart_container']")))
        enter_shopping_cart.click()
        print("click enter shopping cart")

        success_test = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,  "//span[@class='title']")))
        value_success_test = success_test.text
        assert value_success_test == "Your Cart"
        print("test success!")

# создадим переменную, которая будет является экземпляром класса тест_1

test = Test_1()
test.test_select_product()



=======
import time


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from LoginPage import LoginPage

accepted_usernames = ["standard_user", "locked_out_user", "problem_user", "performance_glitch_user"] # создаем список имен

for usernames in accepted_usernames:       # создаем цикл по списку имен
    print(usernames)







class Test_1():

    def test_select_product(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        g = Service('C:\\Users\\user\\PycharmProjects\\resource\\chromedriver.exe')
        driver = webdriver.Chrome(options=options, service=g)
        base_url = 'https://www.saucedemo.com/'
        driver.get(base_url)
        driver.maximize_window()
        time.sleep(5)

        print("Start Test")

        login_standard_user = "standard_user"
        password_all = "secret_sauce"

        login = LoginPage(driver) # создадим переменную, которая будет является экземпляром класса LoginPage
        login.authorization(login_standard_user, password_all)




        select_product = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,  "//button[@id='add-to-cart-sauce-labs-backpack']")))
        select_product.click()
        print("click select product")

        enter_shopping_cart = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,  "//div[@id='shopping_cart_container']")))
        enter_shopping_cart.click()
        print("click enter shopping cart")

        success_test = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,  "//span[@class='title']")))
        value_success_test = success_test.text
        assert value_success_test == "Your Cart"
        print("test success!")

# создадим переменную, которая будет является экземпляром класса тест_1

test = Test_1()
test.test_select_product()



>>>>>>> github/master
