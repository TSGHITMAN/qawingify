import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.mark.usefixtures("setup")
class BaseClass:
    @pytest.fixture(scope="class")
    def setup(self, request):
        service = Service(r"C:\chromedriver.exe")
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(service=service, options=options)
        driver.get("https://sakshingp.github.io/assignment/login.html")
        request.cls.driver = driver
        yield
        driver.close()
