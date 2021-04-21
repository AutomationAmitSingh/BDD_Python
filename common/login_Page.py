from helpers.helper_base import HelperFunc
from selenium import webdriver

class LoginPage(HelperFunc):

    form_id = "kc-form-login"
    usr_id = "username"
    pwd_id = "password"
    login_button_id = "kc-login"


    def __init__(self, driver):
        super(HelperFunc, self).__init__()
        self.driver = webdriver






