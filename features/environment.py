from behave.fixture import use_fixture_by_tag
from selenium import webdriver
import os
from configparser import ConfigParser
from selenium.webdriver.common.keys import Keys
import time
from behave.fixture import use_fixture_by_tag
from helpers.helper_web import setup


def before_all(context):
    config = ConfigParser()
    print((os.path.join(os.getcwd(), 'behave.ini')))
    my_file = (os.path.join(os.getcwd(), 'behave.ini'))
    config.read(my_file)

    # Reading the browser type from the configuration file for Selenium Python Tutorial
    helper_func = setup(config.get('Environment', 'Browser'))
    context.helperfunc = helper_func

    # Local Chrome WebDriver
    # if context.browser == "chrome":
    #   context.driver = webdriver.Chrome()


def after_all(context):
    context.helperfunc.close()
