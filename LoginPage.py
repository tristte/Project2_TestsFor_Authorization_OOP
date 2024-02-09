from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage():

    def __init__(self, driver):
        self.driver = driver

    def authorization(self, login_name, login_password):
        # login_standard_user = "standard_user"
        # password_all = "secret_sauce"
        if login_name == "standard_user":

        user_name = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='user-name']")))
        user_name.send_keys(login_name)  # ввод логина
        print("input login")

        user_password = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='password']")))
        user_password.send_keys(login_password)  # ввод пароля
        print("input password")

        button_login = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='login-button']")))
        button_login.click()
        print("click button_login")
        print("выполняются действия, когда юзер нейм = стандарт")

        elif login_name == "locked_out_user":lllll

        print("выполняются действия, когда юзер нейм = locked out user")