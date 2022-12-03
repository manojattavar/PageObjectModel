from pages.LeadHomepage import LeadHomePage
from pages.base import basepage


class Homepage(basepage):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def homepage(self):
        self.click('crmlink_xpath')
        return LeadHomePage(self.driver)