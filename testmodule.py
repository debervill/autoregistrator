#-*- coding: utf-8  -*
__author__ = 'danamir'

import getmail.py
import proxy.py

driver = webdriver.Firefox(proxy=proxy)

# Переходим по реферальной ссылке
drvr.get("http://bit.ly/1DKTfW2")

# Проверяем наличие datenovost в заголовке
assert "datenovost" in drvr.title

# Ждём 5 секунд
time.clock()
time.sleep(60)

#пароль для регистрации
pwd = "qwerty00"


#переходим на страницу регистрации
drvr.get("http://datenovost.com/registration.html")

#Ищем элемент r-email - почта для регистрации
email = drvr.find_element_by_name("r_email")
email.send_keys(mail)

#ищем поле вводя пароля
passwd =  drvr.find_element_by_name("r_password")
passwd.send_keys(pwd)

#повторный ввод пароля
passwd2 = drvr.find_element_by_name("r_password2")
passwd2.send_keys(pwd)

clck = drvr.find_element_by_name("r_ok")
clck.click()

