from allure_commons.types import AttachmentType
from selenium import webdriver
import allure
import pytest

@allure.severity(allure.severity_level.NORMAL)
class TestJIRA:
    @allure.severity(allure.severity_level.MINOR)
    def test_Logo(self):
        self.driver=webdriver.Chrome("D:\Tools\Python\Driver\Chrome\chromedriver.exe")
        self.driver.get("https://tejira.tataelxsi.co.in/login.jsp")
        logo_status=self.driver.find_element_by_xpath("//*[@id='logo']/a/img").is_displayed()
        if logo_status==True:
            assert True
        else:
            assert False
        self.driver.close()

    @allure.severity(allure.severity_level.MINOR)
    def test_Dashboards(self):
        self.driver=webdriver.Chrome("D:\Tools\Python\Driver\Chrome\chromedriver.exe")
        self.driver.get("https://tejira.tataelxsi.co.in/login.jsp")
        dashboardmenu_status=self.driver.find_element_by_xpath("//*[@id='home_link']").is_displayed()
        if dashboardmenu_status==True:
            assert True
        else:
            assert False
        self.driver.close()

    @allure.severity(allure.severity_level.MINOR)
    def test_Search(self):
        self.driver=webdriver.Chrome("D:\Tools\Python\Driver\Chrome\chromedriver.exe")
        self.driver.get("https://tejira.tataelxsi.co.in/login.jsp")
        search_status=self.driver.find_element_by_xpath("//*[@id='quickSearchInput']").is_displayed()
        if search_status==True:
            assert True
        else:
            assert False
        self.driver.close()

    @allure.severity(allure.severity_level.MINOR)
    def test_Suggestion(self):
        self.driver=webdriver.Chrome("D:\Tools\Python\Driver\Chrome\chromedriver.exe")
        self.driver.get("https://tejira.tataelxsi.co.in/login.jsp")
        suggestionmenu_status=self.driver.find_element_by_xpath("//*[@id='jira-header-feedback-link']").is_displayed()
        if suggestionmenu_status==True:
            assert True
        else:
            assert False
        self.driver.close()

    @allure.severity(allure.severity_level.MINOR)
    def test_Help(self):
        self.driver=webdriver.Chrome("D:\Tools\Python\Driver\Chrome\chromedriver.exe")
        self.driver.get("https://tejira.tataelxsi.co.in/login.jsp")
        helpmenu_status=self.driver.find_element_by_xpath("//*[@id='help_menu']/span").is_displayed()
        if helpmenu_status==True:
            assert True
        else:
            assert False
        self.driver.close()

    @allure.severity(allure.severity_level.MINOR)
    def test_Loginmenu(self):
        self.driver=webdriver.Chrome("D:\Tools\Python\Driver\Chrome\chromedriver.exe")
        self.driver.get("https://tejira.tataelxsi.co.in/login.jsp")
        loginmenu_status=self.driver.find_element_by_xpath("//*[@id='user-options']/a").is_displayed()
        if loginmenu_status==True:
            assert True
        else:
            assert False
        self.driver.close()

    @allure.severity(allure.severity_level.NORMAL)
    def test_Usernamefield(self):
        self.driver=webdriver.Chrome("D:\Tools\Python\Driver\Chrome\chromedriver.exe")
        self.driver.get("https://tejira.tataelxsi.co.in/login.jsp")
        usernamefield_status=self.driver.find_element_by_xpath("//*[@id='login-form-username']").is_displayed()
        if usernamefield_status==True:
            assert True
        else:
            assert False
        self.driver.close()

    @allure.severity(allure.severity_level.NORMAL)
    def test_Passwordfield(self):
        self.driver=webdriver.Chrome("D:\Tools\Python\Driver\Chrome\chromedriver.exe")
        self.driver.get("https://tejira.tataelxsi.co.in/login.jsp")
        passwordfield_status=self.driver.find_element_by_xpath("//*[@id='login-form-password']").is_displayed()
        if passwordfield_status==True:
            assert True
        else:
            assert False
        self.driver.close()

    @allure.severity(allure.severity_level.CRITICAL)
    def test_Login(self):
        self.driver = webdriver.Chrome("D:\Tools\Python\Driver\Chrome\chromedriver.exe")
        self.driver.get("https://tejira.tataelxsi.co.in/login.jsp")
        self.driver.find_element_by_name("os_username").send_keys("madhavikutty.v")
        self.driver.find_element_by_name("os_password").send_keys("Atlanta@1996")
        self.driver.find_element_by_id("login-form-submit").click()
        actual_title=self.driver.title
        if actual_title=="JIRA":
            self.driver.close()
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(),name="JIRALoginScreen",attachment_type=AttachmentType.PNG)
            self.driver.close()
            assert False

