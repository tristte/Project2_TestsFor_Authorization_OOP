import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage():

    def __init__(self, driver):
        self.driver = driver

    def authorization(self, login_name, login_password):

        if login_name == "standard_user":

            user_name_field = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='user-name']")))
            user_name_field.send_keys(login_name)  # ввод логина
            print("input login")

            user_password_field = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='password']")))
            user_password_field.send_keys(login_password)  # ввод пароля
            print("input password")

            button_login = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='login-button']")))
            button_login.click()
            print("click button_login")

        elif login_name == "locked_out_user":
            # driver.refresh   как обновить?
            print("обновить страницу")

        elif login_name == "problem_user":

            user_name_field = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='user-name']")))
            user_name_field.send_keys(login_name)  # ввод логина
            print("input login")

            user_password_field = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='password']")))
            user_password_field.send_keys(login_password)  # ввод пароля
            print("input password")

            button_login = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='login-button']")))
            button_login.click()
            print("click button_login")

        elif login_name == "performance_glitch_user":
        # сделать паузу в 5 сек

            user_name_field = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='user-name']")))
            user_name_field.send_keys(login_name)  # ввод логина
            print("input login")

            user_password_field = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='password']")))
            user_password_field.send_keys(login_password)  # ввод пароля
            print("input password")

            button_login = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='login-button']")))
            button_login.click()
            time.sleep(5)
            print("click button_login")