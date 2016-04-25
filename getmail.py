__author__ = 'danamir'
#-*- coding: utf-8  -*

# -*- coding: utf-8 -*-
__author__ = 'danamir'
import random
import string
ml = ""
lst = "@list.ru"
for i in range(9):
    k = random.choice(string.ascii_letters)
    ml = ml+k
    mail = ml+lst
print(mail)

#Записываем почты в файл
path = '/home/danamir/mail.txt'
f = open(path, 'w')

