 # -*- coding: utf-8 -*-
__author__ = 'danamir'
import time
from selenium import webdriver
    

browser = webdriver.Firefox()
url = "http://bit.ly/1DKTfW2"
browser.get(url)
time.sleep(2)
browser.get("http://datenovost.com/registration.html")



