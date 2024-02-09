from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LogOutPage():

    def __init__(self, driver):
        self.driver = driver

    def logout(self, login_name, login_password):

        if login_name == "standard_user":
            menu_burger = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='react-burger-menu-btn']")))
            menu_burger.click()
            print("нажать на бургер")
            item_logout = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//a[@id='logout_sidebar_link']")))
            item_logout.click()
            print("нажать на пункт меню бургера logout")
        elif login_name == "locked_out_user":
            print("рефрещ")