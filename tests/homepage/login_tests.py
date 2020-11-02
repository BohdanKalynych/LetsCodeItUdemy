from selenium import webdriver
from pages.homepage.login_page import LoginPage
import unittest
import pytest
from utilities.teststatus import TestStatus
import time


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(before='test_validLogin')
    def test_invalidLogin(self):
        self.lp.login(password="qwerty123451")
        #result1 = self.lp.verifyFieldIsEmpty("//input[@id='user_password']", locatorType= "xpath")
        #self.ts.mark(result1, "Password field is empty")
        result2 = self.lp.verifyLoginFailed()
        self.ts.markFinal(self._testMethodName,result2,"Login is failed. Test passed")

    @pytest.mark.run(before='test_validLogout')
    def test_validLogin(self):
        self.lp.login("nerikib@skymailapp.com","qwerty123")
        result1 = self.lp.verifyLoginPageTitle()
        self.ts.mark(result1,"Title is correct")
        result2 = self.lp.verifyLoginSuccess()
        self.ts.markFinal(self._testMethodName,result2,"Login is successful")



    @pytest.mark.run(after='test_validLogin')
    def test_validLogout(self):
        self.lp.logOut()
        result = self.lp.verifyLogOutSuccess()
        self.ts.markFinal(self._testMethodName, result, "Logout is successful")






