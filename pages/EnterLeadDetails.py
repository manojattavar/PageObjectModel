from pages.LeadCheckPage import LeadCheckPage
from pages.base import basepage


class EnterLeadDetail(basepage):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def leaddetails(self, companyname, firstname, lastname):
        self.type('companynametextbox_id', companyname)
        self.type('firstnametextbox_id', firstname)
        self.type('lastnametextbox_id', lastname)
        self.click('saveleadbtn_id')
        self.click('backBtn_xpath')
        return LeadCheckPage(self.driver)

