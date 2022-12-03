import pytest
from conftest import obj_list
from pages.HomePage import Homepage
from pages.LandingPage import LandingPage
from testresources import constants
from testresources.readingexcel import getcelldata, isrunnable
import allure


@pytest.mark.usefixtures("base_fixture")
class TestLead:
    @pytest.mark.parametrize("argvals", getcelldata("CreateLead", constants.XLS_FILEPATH))
    def test_createlead(self, argvals):
        #testcase - firstlevel check
        testrunmode = isrunnable("CreateLead", constants.XLS_FILEPATH)
        #datasheet - secondlevel check
        datarunmode = argvals[constants.RUNMODE]
        if(testrunmode):
            if(datarunmode == constants.RUNMODE_Y):
                for i in range(0, len(obj_list)):
                    pass
                driver = obj_list[i].openbrowser(argvals[constants.BROWSERNAME])
                landing = LandingPage(driver)
                login = landing.landing()
                with allure.step("Loggin In..."):
                    username = login.dologin()
                    password = username.enterusername()
                    homepage = password.enterpassword()
                    if(isinstance(homepage, Homepage)):
                        if(argvals['ExpectedResult']=='Success'):
                            leadhomepage = homepage.homepage()
                            with allure.step("Creating lead....."):
                                enterleaddetails = leadhomepage.addlead()
                                leadcheck = enterleaddetails.leaddetails(argvals['CompanyName'], argvals['FirstName'], argvals['Lastname'])
                        else:
                            obj_list[i].reportfailure("Lead cannot be created")
                        with allure.step("Validating lead creation...."):
                            leadname = argvals['FirstName'] +" "+ argvals['Lastname']
                            obj_list[i].logging(leadname)
                            leadcheck.checklead(leadname)
                    else:
                        obj_list[i].reportfailure("Login Failed!!!")
            else:
                pytest.skip("Testcase skipped due to run mode is no on data sheet")
        else:
            pytest.skip("Testcase skipped due to run mode is no on test sheet")