# from datetime import datetime, timedelta
#
# # Получаем текущую дату
# current_date = datetime.now()
#
# # Добавляем 10 дней к текущей дате
# new_date = current_date + timedelta(days=10)
#
# # Выводим новую дату
# print("Новая дата через 10 дней:", new_date)

# print(round(1/3, 2))
# b = 3
# b = b * b
# b = b + b * b
# print(b)

# WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='visibleAfter']"))) # шаблон для работы с явными ожиданиями


# user_name = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,  "//input[@id='user-name']"))) # выбор поля логин
# user_name.send_keys(login_standard_user)  # ввод логина
# print("input login")
#
# user_password = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,  "//input[@id='password']"))) # выбор поля пароль
# user_password.send_keys(password_all)  # ввод пароля
# print("input password")
#
# button_login = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,  "//input[@id='login-button']")))  # выбор кнопки login
# button_login.click()
# print("click button_login")


print('Гвидо', 'Ван', 'Россум', sep='*', end='-')
print('Основатель', 'Питона', sep='_', end='!')