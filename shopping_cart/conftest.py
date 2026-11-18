import pytest
from selenium import webdriver

from login_page.login_page import LoginPage


@pytest.fixture
def driver():

    driver = webdriver.Chrome()
    driver.implicitly_wait(10)

    login_page = LoginPage(driver)
    login_page.load()
    login_page.log_in("test1337@gmail.com","1234qwer")


    yield driver

    driver.quit()