from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    amount = (By.XPATH, "//th[@id='amount']")
    amountElements = (By.XPATH, "//tr/td[5]")

    def getAmount(self):
        return self.driver.find_element(*HomePage.amount)

    def getWebElements(self):
        return self.driver.find_elements(*HomePage.amountElements)

