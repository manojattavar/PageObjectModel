import logging
import time
from _overlapped import NULL
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from _datetime import datetime
import conftest
from testresources import constants
global driver


class basepage:
    def __init__(self):
        self.driver = NULL
        self.prod = conftest.prod
        self.logger = logging.getLogger()

    def openbrowser(self, browsername):
        with allure.step("Opening browser : "+browsername):
            if(self.prod['GridRun'] == constants.GRIDRUN_Y):
                if(browsername == constants.CHROME):
                    caps = DesiredCapabilities.CHROME.copy()
                    caps['browserName'] = 'chrome'
                    caps['javascriptEnabled'] = True
                elif(browsername == constants.FIREFOX):
                    caps = DesiredCapabilities.FIREFOX.copy()
                    caps['browserName'] = 'firefox'
                    caps['javascriptEnabled'] = True
                elif(browsername == constants.EDGE):
                    caps = DesiredCapabilities.EDGE.copy()
                    caps['browserName'] = 'MicrosoftEdge'
                    caps['javascriptEnabled'] = True
                else:
                    caps = DesiredCapabilities.INTERNETEXPLORER.copy()
                    caps['browserName'] = 'internet explorer'
                    caps['javascriptEnabled'] = True
                try:
                    self.driver = webdriver.Remote(desired_capabilities=caps,
                                                   command_executor='http://192.168.0.101:4444/wd/hub')
                except Exception as e:
                    print(e)
            else:
                if(browsername == constants.CHROME):
                    options = webdriver.ChromeOptions()
                    options.add_argument("--disable-infobars")
                    options.add_argument("--disable-notifications")
                    options.add_argument("--start-maximized")
                    self.driver = webdriver.Chrome(options=options)
                elif(browsername == constants.FIREFOX):
                    fp = webdriver.FirefoxProfile(
                        "C:\\Users\\Abhishek\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\dslne5iu.Jaspreet")
                    fp.set_preference("dom.webnotification.enabled", False)
                    fp.accept_untrusted_certs = True
                    self.driver = webdriver.Firefox(fp)
                elif(browsername == constants.EDGE):
                    self.driver = webdriver.Edge()
                    self.driver.maximize_window()
                else:
                    self.driver = webdriver.Ie()
                    self.driver.maximize_window()
            self.takescreenshot()
            return self.driver

    def navigate(self):
        url = self.prod['URL']
        with allure.step("Navigating to : " +url):
            self.driver.get(url)
            self.takescreenshot()

    def click(self, obj):
        with allure.step("Clicking on : " + obj):
            self.getelement(obj).click()
            self.takescreenshot()

    def type(self, obj, data):
        with allure.step("Typing in : " +obj+ " with : "+data):
            self.getelement(obj).send_keys(data)
            self.takescreenshot()


    #common utility
    def takescreenshot(self):
        allure.attach(self.driver.get_screenshot_as_png(), "Screenshot at : " + str(datetime.now()),
                      AttachmentType.PNG)

    def waitforpagetobeloaded(self):
        i=1
        while(i!=10):
            load_status = self.driver.execute_script("return document.readyState")
            if(load_status == 'complete'):
                break
            else:
                time.sleep(2)

    def iselementpresent(self, obj):
        wait = WebDriverWait(self.driver, 20)
        element = self.prod[obj]
        self.waitforpagetobeloaded()
        if (obj.endswith('_xpath')):
            elementlist = wait.until(EC.presence_of_all_elements_located((By.XPATH, element)))
        elif (obj.endswith('_id')):
            elementlist = wait.until(EC.presence_of_all_elements_located((By.ID, element)))
        elif (obj.endswith('_name')):
            elementlist = wait.until(EC.presence_of_all_elements_located((By.NAME, element)))
        elif (obj.endswith('_cssSelector')):
            elementlist = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, element)))
        else:
            elementlist = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, element)))
        if(len(elementlist)==0):
            return False
        else:
            return True

    def iselementvisible(self, obj):
        wait = WebDriverWait(self.driver, 20)
        element = self.prod[obj]
        self.waitforpagetobeloaded()
        if (obj.endswith('_xpath')):
            elementlist = wait.until(EC.visibility_of_all_elements_located((By.XPATH, element)))
        elif (obj.endswith('_id')):
            elementlist = wait.until(EC.visibility_of_all_elements_located((By.ID, element)))
        elif (obj.endswith('_name')):
            elementlist = wait.until(EC.visibility_of_all_elements_located((By.NAME, element)))
        elif (obj.endswith('_cssSelector')):
            elementlist = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, element)))
        else:
            elementlist = wait.until(EC.visibility_of_all_elements_located((By.TAG_NAME, element)))
        if (len(elementlist) == 0):
            return False
        else:
            return True

    def getelement(self, locator):
        obj = self.prod[locator]
        if(self.iselementpresent(locator) and self.iselementvisible(locator)):
            try:
                if(locator.endswith('_xpath')):
                    element = self.driver.find_element(By.XPATH, obj)
                elif (locator.endswith('id')):
                    element = self.driver.find_element(By.ID, obj)
                elif (locator.endswith('_name')):
                    element = self.driver.find_element(By.NAME, obj)
                elif(locator.endswith('_cssSelector')):
                    element = self.driver.find_element(By.CSS_SELECTOR, obj)
                else:
                    return False
                return element
            except Exception:
                print("Element not found")
        else:
            print("Element either not present or visible")

    def quit(self):
        if(self.driver!=NULL):
            self.driver.quit()

    def logging(self, message):
        self.logger.setLevel(logging.INFO)
        self.logger.info(message)

    def reportfailure(self, message):
        self.takescreenshot()
        assert False, message

    def reportsuccess(self, message):
        self.logging(message)
        assert True

    def wait(self):
        time.sleep(2)

    #validate functions
    def validatetitle(self):
        expectedtitle = self.prod['expectedhomepagetitle']
        actualtitle = self.driver.title
        if(actualtitle==expectedtitle):
            self.logging("Title validation successful")
        else:
            self.logging("Title validation failed..Got title as "+actualtitle+ " instead of "+expectedtitle)
            #report failure

    def getrowcount(self,name):
        rows = self.driver.find_elements_by_xpath(self.prod['allLeads_xpath'])
        for rnum in range(0, len(rows)):
            if((rows[rnum].text)==name):
                return rnum+1
        return -1

    def clickleadname(self, name):
        rnum = self.getrowcount(name)
        element = self.driver.find_element_by_xpath(self.prod['leadnamepart1_xpath']+str(rnum)+self.prod['leadnamepart2_xpath'])
        element.click()

    def selectdate(self, date):
        with allure.step("Selecting date : " + date):
            dt = datetime.strptime(date, "%d-%m-%Y")
            year = dt.year
            month = dt.strftime("%B")
            day = dt.day
            desired_date = month + " " + str(year)
            while True:
                displayed_date = self.driver.find_element_by_xpath("//*[@id='calenDiv']/div/div[1]/div/span[3]").text
                if (desired_date > displayed_date):
                    self.driver.find_element_by_id("pm").click()
                    displayed_date = self.driver.find_element_by_xpath("//*[@id='calenDiv']/div/div[1]/div/span[3]").text
                    if (displayed_date == desired_date):
                        self.driver.find_element_by_xpath("//td[text()=" + str(day) + "]").click()
                        break
                elif (desired_date < displayed_date):
                    self.driver.find_element_by_id("nm").click()
                    displayed_date = self.driver.find_element_by_xpath("//*[@id='calenDiv']/div/div[1]/div/span[3]").text
                    if (displayed_date == desired_date):
                        self.driver.find_element_by_xpath("//td[text()=" + str(day) + "]").click()
                        break
            self.takescreenshot()




