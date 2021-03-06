import configparser

config = configparser.RawConfigParser()
config.read(".\\behave.ini")


class ReadConfig:
    @staticmethod
    def get_application_url():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def get_user_email():
        username = config.get('common info', 'userEmail')
        return username

    @staticmethod
    def get_password():
        password = config.get('common info', 'password')
        return password

    @staticmethod
    def get_login_data_path():
        path = config.get('common info', 'loginDataPath')
        return path
