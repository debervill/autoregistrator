#-*- coding: utf-8  -*
__author__ = 'danamir'


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.proxy import *
import time
import string
import random
import os


#Генерируем из набора в 9 символов адрес почты и выводим его

ml = ""
lst = "@list.ru"
for i in range(9):
    k = random.choice(string.ascii_letters)
    ml = ml+k
    mail = ml+lst
print(mail)

#Записываем почты в файл
path = '/home/danamir/mail.txt'
f = open(path, w)


#Запускаем бота через прокси

myProxy = "62.176.13.22:8088"
proxy = Proxy({
    'proxyType': ProxyType.MANUAL,
    'httpProxy': myProxy,
    'ftpProxy': myProxy,
    'sslProxy': myProxy,
    'noProxy': '' # set this value as desired
    })

drvr = webdriver.Firefox(proxy=proxy)

# Переходим по реферальной ссылке
drvr.get("http://bit.ly/1DKTfW2")

# Проверяем наличие datenovost в заголовке
assert "datenovost" in drvr.title


# Ждём 5 секунд
time.clock()time.sleep(60)

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

