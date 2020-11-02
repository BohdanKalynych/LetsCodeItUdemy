from pages.courses.register_courses_page import RegisterCoursesPage
import unittest
import pytest
from utilities.teststatus import TestStatus
import time


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class RegisterCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_invallid_enrollment(self):
        self.courses.enterCourseName("JavaScript for beginners")
        self.courses.selectCourseToEnroll("JavaScript for beginners")
        self.courses.enrollCourse(num="4485 5854 8176 7883",
                                  exp="1222",
                                  cvv="123",
                                  postalCode="79002")
        self.courses.acceptTermsAndConditions()
        self.courses.clickEnrollSubmitButton()
        result = self.courses.verifyEnrollFailed()
        self.ts.markFinal(self._testMethodName,result,"Enrollment Failed verification ")



