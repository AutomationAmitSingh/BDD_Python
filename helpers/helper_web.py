from selenium import webdriver
from helpers.helper_base import HelperFunc


def setup(browser):
    if browser == 'chrome':
        driver = HelperFunc(webdriver.Chrome())
        print("Launching chrome browser.........")
    elif browser == 'firefox':
        driver = HelperFunc(webdriver.Firefox())
        print("Launching firefox browser.........")
    return driver
