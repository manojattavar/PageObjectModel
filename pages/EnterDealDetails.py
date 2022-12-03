from selenium.webdriver.common.keys import Keys

from pages.DealCheckPage import DealCheckPage
from pages.base import basepage


class EnterDealDetails(basepage):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def leaddetails(self, dealname, accountname, stage, closingdate):
        self.type('DealNametxtBox_id',dealname)
        self.type('account_id', accountname)
        self.type('stage_xpath', stage)
        self.click('closingDate_id')
        self.selectdate(closingdate)
        self.getelement('closingDate_id').send_keys(Keys.ENTER)
        self.click('backBtn_xpath')
        return DealCheckPage(self.driver)

