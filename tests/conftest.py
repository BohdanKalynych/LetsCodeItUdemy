import pytest
from base.webdriverfactory import WebDriverFactory
from pages.homepage.login_page import LoginPage

@pytest.yield_fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")


@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request, browser):
    print("Running one time setUp")
    wbf = WebDriverFactory(browser)
    driver= wbf.getWebDriverInstance()
    lp = LoginPage(driver)
    lp.login("nerikib@skymailapp.com","qwerty123")

    # if browser == 'firefox':
    #     baseURL = "https://letskodeit.teachable.com/"
    #     driver = webdriver.Firefox()
    #     driver.maximize_window()
    #     driver.implicitly_wait(3)
    #     driver.get(baseURL)
    #     print("Running tests on FF")
    # else:
    #     baseURL = "https://letskodeit.teachable.com/"
    #     driver = webdriver.Chrome()
    #     driver.maximize_window()
    #     driver.implicitly_wait(3)
    #     driver.get(baseURL)
    #     print("Running tests on chrome")

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    #driver.quit()
    print("Running one time tearDown")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")
