from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LogOutPage():

    def __init__(self, driver):
        self.driver = driver

    def logout(self, login_name, login_password):

        if login_name == "standard_user":
            print("Выход")


        elif login_name == "locked_out_user":

        print("выполняются действия, когда юзер нейм = locked out user")