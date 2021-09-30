import pytest
from backend import init_app
from selenium import webdriver
from time import sleep

# time to wait the page to load
TIME=1

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
    def test_bad_register(self):
        self.driver.get("http://localhost:8000/user/register")
        sleep(TIME)
        assert "user/register" in self.driver.current_url

        self.driver.find_element_by_id("username").send_keys('newuser1')

        # test bad mail format
        self.driver.find_element_by_id("email").send_keys('badmail')
        self.driver.find_element_by_id("password").send_keys('123456789')
        self.driver.find_element_by_id("retype_password").send_keys('123456789')
        self.driver.find_element_by_id("signUp").click()
        sleep(TIME)
        errors = self.driver.find_elements_by_class_name("errors")
        assert errors[0].text == "Invalid Email"
        
        # test bad password format 
        self.driver.find_element_by_id("email").send_keys('newuser1@correo.com')
        self.driver.find_element_by_id("password").send_keys('123456789')
        self.driver.find_element_by_id("retype_password").send_keys('123456789')
        self.driver.find_element_by_id("signUp").click()
        sleep(TIME)
        errors = self.driver.find_elements_by_class_name("errors")
        assert errors[0].text == "Password must have at least 6 characters with one lowercase letter, one uppercase letter and one number"

        # test password not math
        self.driver.find_element_by_id("password").send_keys('Aa123456789')
        self.driver.find_element_by_id("retype_password").send_keys('aA123456789')
        self.driver.find_element_by_id("signUp").click()
        sleep(TIME)
        errors = self.driver.find_elements_by_class_name("errors")
        assert errors[0].text == "Password and Retype Password did not match"


    def test_sign_up(self):
        self.driver.get("http://localhost:8000/welcome")
        sleep(TIME)
        assert self.driver.title == "DEGVA"

        self.driver.find_element_by_id("signUp").click()
        sleep(TIME)
        assert "user/register" in self.driver.current_url

        self.driver.find_element_by_id("username").send_keys('newuser')
        self.driver.find_element_by_id("email").send_keys('newuser@correo.com')
        self.driver.find_element_by_id("password").send_keys('Aa123456789')
        self.driver.find_element_by_id("retype_password").send_keys('Aa123456789')
        
        self.driver.find_element_by_id("signUp").click()
        sleep(TIME)

        assert "check_email" in self.driver.current_url

    def test_user_exist(self):
        self.driver.get("http://localhost:8000/user/register")
        sleep(TIME)
        assert "user/register" in self.driver.current_url

        self.driver.find_element_by_id("username").send_keys('newuser')
        self.driver.find_element_by_id("email").send_keys('newuser@correo.com')
        self.driver.find_element_by_id("password").send_keys('Aa123456789')
        self.driver.find_element_by_id("retype_password").send_keys('Aa123456789')

        self.driver.find_element_by_id("signUp").click()
        sleep(TIME)
        errors = self.driver.find_elements_by_class_name("errors")
        assert errors[0].text == "This Username is already in use. Please try another one."

        self.driver.find_element_by_id("username").send_keys('newuser1')
        self.driver.find_element_by_id("email").send_keys('newuser@correo.com')
        self.driver.find_element_by_id("password").send_keys('Aa123456789')
        self.driver.find_element_by_id("retype_password").send_keys('Aa123456789')

        self.driver.find_element_by_id("signUp").click()
        sleep(TIME)
        errors = self.driver.find_elements_by_class_name("errors")
        assert errors[0].text == "This Email is already in use. Please try another one."

    def test_bad_login(self):
        self.driver.get('http://localhost:8000/user/sign-in')
        sleep(TIME)
        assert self.driver.title == "Log In"

        self.driver.find_element_by_id("username").send_keys('baduser')
        self.driver.find_element_by_id("password").send_keys('badpassword')
        self.driver.find_element_by_id("signIn").click()

        sleep(TIME)

        assert self.driver.find_element_by_id("errors").text == "Incorrect Username/Email and/or Password"

        # test short password
        self.driver.find_element_by_id("username").send_keys('newuser@correo.com')
        self.driver.find_element_by_id("password").send_keys('1')
        self.driver.find_element_by_id("signIn").click()

        sleep(TIME)

        assert self.driver.find_element_by_id("errors").text == "El campo debe tener al menos 8 caracteres."

    def test_facebook_button(self):
        self.driver.get('http://localhost:8000/user/sign-in')
        sleep(TIME)
        assert self.driver.title == "Log In"

        self.driver.find_element_by_id("facebook").click()

        sleep(TIME)
        assert "facebook.com" in self.driver.current_url

    def test_login_user(self):
        self.driver.get("http://localhost:8000/welcome")
        sleep(TIME)
        assert "DEGVA" in self.driver.title

        self.driver.find_element_by_id("logIn").click()
        sleep(TIME)
        assert "user/sign-in" in self.driver.current_url 

        self.driver.find_element_by_id("username").send_keys('test_user@correo.com')
        self.driver.find_element_by_id("password").send_keys('Aa123456789')
        self.driver.find_element_by_id("signIn").click()

        sleep(TIME)

        assert "DEGVA" in self.driver.title 

    def test_log_out(self):
        self.driver.get("http://localhost:8000/")
        sleep(TIME)
        assert self.driver.title == "DEGVA"

        self.driver.find_element_by_id("logOut").click()
        sleep(TIME)
        assert "welcome" in self.driver.current_url

    def test_forgot_password(self):
        self.driver.get("http://localhost:8000/user/sign-in")
        sleep(TIME)
        assert self.driver.title == "Log In"

        self.driver.find_element_by_id("linkpassword").click()
        sleep(TIME)
        assert "Forgot Password" in self.driver.title

        self.driver.find_element_by_id("linkpassword").send_keys("newuser@correo.com")
        self.driver.find_element_by_id("send").click()
        sleep(TIME)
        assert "check_email" in self.driver.current_url
