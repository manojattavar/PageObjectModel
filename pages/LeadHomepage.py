from pages.EnterDealDetails import EnterDealDetails
from pages.EnterLeadDetails import EnterLeadDetail
from pages.base import basepage


class LeadHomePage(basepage):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def addlead(self):
        self.click('leadtab_xpath')
        self.click('addiconbtn_xpath')
        return EnterLeadDetail(self.driver)

    def convertlead(self, name):
        self.click('leadtab_xpath')
        self.wait()
        rnum = self.getrowcount(name)
        if(rnum==-1):
            self.reportfailure("Lead name "+name+" not found in the table")
        else:
            self.clickleadname(name)
            self.click('convertbtn_xpath')
            self.click('confirmconvertbtn_id')
            self.click('gotoleadsbtn_xpath')
            rnum = self.getrowcount(name)
            if (rnum == -1):
                self.reportsuccess("Lead name "+name+" got converted")
            else:
                self.reportfailure("Lead name "+name+" not converted...lying at row no. : "+str(rnum))

    def deletelead(self, name):
        self.click('leadtab_xpath')
        self.wait()
        rnum = self.getrowcount(name)
        if (rnum == -1):
            self.reportfailure("Lead name " + name + " not found in the table")
        else:
            self.clickleadname(name)
            self.click('options_id')
            self.click('deletebtn_xpath')
            self.click('confirmdeletebtn_xpath')
            rnum = self.getrowcount(name)
            if (rnum == -1):
                self.reportsuccess("Lead name "+name+" got deleted")
            else:
                self.reportfailure("Lead name "+name+" not deleted...lying at row no. : "+str(rnum))

    def adddeal(self):
        self.click('dealtab_xpath')
        self.click('addiconbtn_xpath')
        return EnterDealDetails(self.driver)

    def deletedeal(self, name):
        self.click('dealtab_xpath')
        self.wait()
        rnum = self.getrowcount(name)
        if (rnum == -1):
            self.reportfailure("Deal name " + name + " not found in the table")
        else:
            self.clickleadname(name)
            self.click('options_id')
            self.click('deletebtn_xpath')
            self.click('confirmdeletebtn_xpath')
            rnum = self.getrowcount(name)
            if (rnum == -1):
                self.reportsuccess("Deal name "+name+" got deleted")
            else:
                self.reportfailure("Deal name "+name+" not deleted...lying at row no. : "+str(rnum))