from pages.base import basepage


class LeadCheckPage(basepage):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def checklead(self, name):
        self.wait()
        rNum = self.getrowcount(name)
        if(rNum==-1):
            self.reportfailure("Lead name "+name+" not found in the table")
        else:
            self.reportsuccess("Lead name "+name+" found at row no. : "+str(rNum))