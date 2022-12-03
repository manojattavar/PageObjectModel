from pages.EnterUsername import EnterUsername
from pages.base import basepage


class LoginPage(basepage):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def dologin(self):
        self.click('loginlink_xpath')
        return EnterUsername(self.driver)