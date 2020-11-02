from base.basepage import BasePage
import utilities.custom_logger as cl
import logging
import time


class RegisterCoursesPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    ### Locators
    _search_box = "//input[@id='search-courses']"
    _course = "//div[contains(@class,'course-listing-title') and contains(text(),'{0}')]"
    _all_courses = "//div[@class='row course-list list']"
    _enroll_button = "//button[@id='enroll-button-top']"
    _payment_method_dropdown = "//select[@name='dropdown_select']"
    _cc_num = "//input[@aria-label='Credit or debit card number']"
    _cc_num_iframe ="__privateStripeFrame5"
    _cc_exp = "//input[@aria-label='Credit or debit card expiration date']"
    _cc_exp_iframe = "__privateStripeFrame6"
    _cc_cvv = "//input[@aria-label='Credit or debit card CVC/CVV']"
    _cc_cvv_iframe = "__privateStripeFrame7"
    _country_dropdown = "//select[@id='country_code_credit_card-cc']"
    _postal_code = "//input[@name='postal']"
    _postal_code_iframe = "__privateStripeFrame8"
    _submit_enroll = "//button[@id='confirm-purchase']//label"
    _enroll_error_message = "//div[@class='payment-error-box only-on-mobile']//span[contains(text(),'The card was declined.')]"
    _terms_checkbox = "//input[@id='agreed_to_terms_checkbox']"



    def enterCourseName(self, name):
        self.sendKeys(name, locator=self._search_box)

    def selectCourseToEnroll(self, courseName):
        self.elementClick(locator=self._course.format(courseName))

    def clickEnrollButton(self):
        self.waitForElement(locator=self._enroll_button)
        self.elementClick(locator=self._enroll_button)

    def selectPaymentMethod(self, paymentMethodName):
        self.selectDropDownValue(dropDownValue=paymentMethodName, locator=self._payment_method_dropdown)

    def selectCountry(self, coutryName):
        self.selectDropDownValue(dropDownValue=coutryName, locator=self._country_dropdown)

    def enterPostalCode(self, postalCode):
        self.switchToFrame(name="__privateStripeFrame8")
        self.sendKeys(postalCode, locator=self._postal_code)
        self.switchToDefaultContent()

    def enterCardNum(self, num):
        self.switchToFrame(name="__privateStripeFrame5")
        self.elementClick(locator=self._cc_num)
        self.sendKeys(num,locator=self._cc_num)
        self.switchToDefaultContent()


    def enterCardExp(self, exp):
        self.switchToFrame(name="__privateStripeFrame6")
        self.sendKeys(exp, locator=self._cc_exp)
        self.switchToDefaultContent()

    def enterCardCvv(self, cvv):
        self.switchToFrame(name="__privateStripeFrame7")
        self.sendKeys(cvv, locator=self._cc_cvv)
        self.switchToDefaultContent()

    def clickEnrollSubmitButton(self):
        self.elementClick(locator=self._submit_enroll)

    def enterCreditCardInfo(self, paymentMethodName, num, exp, cvv, countryName, postalCode):
        #self.selectPaymentMethod(paymentMethodName)
        self.enterCardNum(num)
        self.enterCardExp(exp)
        self.enterCardCvv(cvv)
        #self.selectCountry(countryName)
        self.enterPostalCode(postalCode)

    def enrollCourse(self, paymentMethodName="", num="", exp="", cvv="", countryName="", postalCode=""):
        self.clickEnrollButton()
        self.webScroll(direction="down")
        self.enterCreditCardInfo(paymentMethodName, num, exp, cvv, countryName, postalCode)
        #self.clickEnrollSubmitButton()

    def verifyEnrollFailed(self):
        messageElement= self.waitForElement(locator=self._enroll_error_message)
        result = self.isElementDisplayed(element=messageElement)
        return result

    def acceptTermsAndConditions(self):
        self.elementClick(locator=self._terms_checkbox)

