import time

from pageobject.HomePage import HomePage
from pageobject.LoginPage import LoginPage
from tests.coftest import BaseClass


class TestLogin(BaseClass):

    def test_login(self):
        loginPage = LoginPage(self.driver)
        loginPage.getEmail().send_keys("test@gmail.com")
        loginPage.getPassword().send_keys("1234")
        loginPage.log_In().click()
        browserSortedAmount = []
        time.sleep(2)
        homePage = HomePage(self.driver)
        homePage.getAmount().click()
        webElements = homePage.getWebElements()
        for ele in webElements:
            browserSortedAmount.append(ele.text)

        originalSortedAmount = browserSortedAmount.copy()
        browserSortedAmount.sort()
        assert browserSortedAmount == originalSortedAmount

