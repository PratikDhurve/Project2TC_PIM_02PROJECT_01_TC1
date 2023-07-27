import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage

class test_001_Login:
    baseURL="https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    username="Admin"
    password="admin123"

    def test_homePageTitle(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        self.driver.close()
        if act_title == "OrangeHRM":
           assert True
        else:
           assert False


    def test_login(self,setup):
        self.driver=setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage (self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title
        self.driver.close()
        if act_title == "OrangeHRM":
           assert True
        else:
           assert False


