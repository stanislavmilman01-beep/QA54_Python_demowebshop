from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time

URL = "https://demowebshop.tricentis.com/"
email = f"qa_{int(time.time())}@example.com"
#time абсолютно гениальная штука <3
password = "Test123!"

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(URL)

    yield driver

    driver.quit()


def test_registration_story(driver):

    driver.find_element(By.CSS_SELECTOR,"a.ico-register").click()

    driver.find_element(By.ID,"gender-male").click()
    driver.find_element(By.ID,"FirstName").send_keys("Stas")
    driver.find_element(By.ID,"LastName").send_keys("Tesman")
    driver.find_element(By.ID,"Email").send_keys(email)
    driver.find_element(By.ID,"Password").send_keys(password)
    driver.find_element(By.ID,"ConfirmPassword").send_keys(password)

    driver.find_element(By.ID,"register-button").click()

    result = driver.find_element(By.CSS_SELECTOR, "div.result")
    assert result.text == "Your registration completed"


def test_login(driver):

    driver.find_element(By.CSS_SELECTOR,"a.ico-login").click()

    driver.find_element(By.ID, "Email").send_keys(email)
    driver.find_element(By.ID,"Password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR,"input.login-button").click()

    result = driver.find_element(By.CSS_SELECTOR,"a.account")
    assert result.text == email
