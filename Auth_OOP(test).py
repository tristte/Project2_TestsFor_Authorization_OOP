import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from LogOutPage import LogOutPage
from LoginPage import LoginPage

class Test_1():

    def test_LogIn_LogOut(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        g = Service('C:\\Users\\user\\PycharmProjects\\resource\\chromedriver.exe')
        driver = webdriver.Chrome(options=options, service=g)
        base_url = 'https://www.saucedemo.com/'
        driver.get(base_url)
        driver.maximize_window()
        time.sleep(5)

        print("Start Test")
        password_all = "secret_sauce"
        accepted_usernames = ["standard_user", "locked_out_user", "problem_user", "performance_glitch_user"]  # создаем список имен

        for username in accepted_usernames:  # создаем цикл по списку имен
            print("Создаем объект класса LoginPage")
            login = LoginPage(driver)  # создадим переменную, которая будет является экземпляром класса LoginPage
            print("Выполняем авторизацию для пользователя: " + username)
            login.authorization(username, password_all)

            print("Создаем объект класса LogoutPage")
            logout = LogOutPage(driver)
            logout.logout(username, password_all)
            print("Выполняем выход для пользователя: " + username)








# создадим переменную, которая будет является экземпляром класса тест_1
test = Test_1()
test.test_LogIn_LogOut()