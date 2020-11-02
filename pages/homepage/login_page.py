from base.selenium_driver import SeleniumDriver
from base.basepage import BasePage
import utilities.custom_logger as cl
import logging
import time

class LoginPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _login_link = "//a[@class='navbar-link fedora-navbar-link']"
    _email_field = "//input[@name='user[email]']"
    _password_field = "//input[@name='user[password]']"
    _login_button = "//input[@name='commit']"
    _logOut_button = "//a[@href='/sign_out']"
    _user_icon = "//img[@class='gravatar']"

    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="xpath")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field, locatorType="xpath")

    def enterPassword(self, password):
        self.sendKeys(password,self._password_field, locatorType="xpath")

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="xpath")

    def login(self, email="", password=""):
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginSuccess(self):
        result = self.isElementPresent(self._user_icon,
                                       locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("//div[contains(text(),'Invalid email or password.')]",
                                       locatorType="xpath")
        return result

    def verifyLoginPageTitle(self):
        return self.verifyPageTitle("Let's Kode It")


    def verifyLogOutSuccess(self):
        result = self.isElementPresent("//img[@class='gravatar']",
                                      locatorType="xpath")
        return result

    def clickUserIcon(self):
        self.elementClick(self._user_icon, locatorType="xpath")
        time.sleep(1 )

    def clickLogOutButton(self):
        self.elementClick(self._logOut_button, locatorType="xpath")

    def logOut(self):
        self.clickUserIcon()

        self.clickLogOutButton()





