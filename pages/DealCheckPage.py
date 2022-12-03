from pages.base import basepage


class DealCheckPage(basepage):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def checkdeal(self, name):
        self.wait()
        rNum = self.getrowcount(name)
        if(rNum==-1):
            self.reportfailure("Deal name "+name+" not found in the table")
        else:
            self.reportsuccess("Deal name "+name+" found at row no. : "+str(rNum))