import time
#external files - properties , xlsx, csv....
#properties - locator
#excel - testdata
from pages.EnterPassword import EnterPassword
from pages.base import basepage


class EnterUsername(basepage):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def enterusername(self):
        self.type('usernametextbox_id', self.prod['defaultusername'])
        self.click('submitemailbtn_xpath')
        return EnterPassword(self.driver)

