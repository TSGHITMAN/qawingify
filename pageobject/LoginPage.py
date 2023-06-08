from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    username = (By.ID, "username")
    password = (By.ID, "password")
    login = (By.ID, "log-in")

    def getEmail(self):
        return self.driver.find_element(*LoginPage.username)

    def getPassword(self):
        return self.driver.find_element(*LoginPage.password)

    def log_In(self):
        return self.driver.find_element(*LoginPage.login)
