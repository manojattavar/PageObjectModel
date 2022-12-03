import time
#external files - properties , xlsx, csv....
#properties - locator
#excel - testdata
from pages.HomePage import Homepage
from pages.base import basepage


class EnterPassword(basepage):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def enterpassword(self):
        self.type('passwordtextbox_id', self.prod['defaultpassword'])
        self.click('signinbtn_xpath')
        #homepage - zoho crm
        #wrong - stay on same page
        # obj - homepage
        return Homepage(self.driver)
