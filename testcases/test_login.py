import pytest
from conftest import obj_list
from pages.HomePage import Homepage
from pages.LandingPage import LandingPage
from testresources import constants
from testresources.readingexcel import getcelldata, isrunnable
import allure


@pytest.mark.usefixtures("base_fixture")
class TestLogin:
    @pytest.mark.parametrize("argvals", getcelldata("LoginTest", constants.XLS_FILEPATH))
    def test_login(self, argvals):
        #testcase - firstlevel check
        testrunmode = isrunnable("LoginTest", constants.XLS_FILEPATH)
        #datasheet - secondlevel check
        datarunmode = argvals[constants.RUNMODE]
        if(testrunmode):
            if(datarunmode == constants.RUNMODE_Y):
                for i in range(0, len(obj_list)):
                    pass
                driver = obj_list[i].openbrowser(argvals[constants.BROWSERNAME])
                landing = LandingPage(driver)
                login = landing.landing()
                username = login.dologin()
                password = username.enterusername()
                homepage = password.enterpassword()
                with allure.step("Validating Login..."):
                    if(isinstance(homepage, Homepage)):
                        if(argvals['ExpectedResult']=='Success'):
                            homepage.homepage()
                        else:
                            obj_list[i].reportfailure("Expected result was not success")
                    else:
                        obj_list[i].reportfailure("Login Failed!!!")
            else:
                pytest.skip("Testcase skipped due to run mode is no on data sheet")
        else:
            pytest.skip("Testcase skipped due to run mode is no on test sheet")