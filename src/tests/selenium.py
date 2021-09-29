import pytest
from selenium import webdriver
from time import sleep

#Fixture for Chrome
@pytest.fixture(scope="class")
def chrome_driver_init(request):
    chrome_driver = webdriver.Chrome()
    request.cls.driver = chrome_driver
    yield
    chrome_driver.close()

@pytest.mark.usefixtures("chrome_driver_init")
class Basic_Chrome_Test:
    pass

class TestLoginPage(Basic_Chrome_Test):
    def test_login_user(self):
        self.driver.get('http://localhost:8000/user/sign-in')
        sleep(2)
        assert self.driver.title == "Log In"

        self.driver.find_element_by_id("username").send_keys('owner@vittorioadesso.com')
        self.driver.find_element_by_id("password").send_keys('26838989')
        self.driver.find_element_by_id("signIn").click()

        sleep(2)

        assert self.driver.title == "DEGVA"

    def test_log_out(self):
        self.driver.get("http://localhost:8000/")
        sleep(2)
        assert self.driver.title == "DEGVA"

        self.driver.find_element_by_id("logOut").click()
        sleep(2)
        assert self.driver.title == "DEGVA"
        assert self.driver.find_element_by_id("logIn").text == "LOG IN"


    # def test_bad_login(self):
    #     self.driver.get('http://localhost:8000/user/sign-in')
    #     sleep(2)
    #     assert self.driver.title == "Log In"






