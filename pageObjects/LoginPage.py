from selenium import webdriver


class LoginPage:
    textbox_username_xpath = "//*[@placeholder='Username']"
    textbox_password_xpath = "//*[@type='password']"
    button_login_xpath = "//*[@type='submit']"

    def _init_(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element_by_xpath(self.textbox_username_xpath).send_keys(username).clear()
        self.driver.find_element_by_xpath(self.textbox_username_xpath).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_xpath(self.textbox_password_xpath).send_keys(password).clear()
        self.driver.find_element_by_xpath(self.textbox_password_xpath).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()
