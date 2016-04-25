__author__ = 'danamir'
from selenium.webdriver.common.proxy import *
myProxy = "82.147.82.228:8080"
proxy = Proxy({
    'proxyType': ProxyType.MANUAL,
    'httpProxy': myProxy,
    'ftpProxy': myProxy,
    'sslProxy': myProxy,
    'noProxy': '' # set this value as desired
    })
