from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class RegistrationPage:

    REGISTRATION_LINK = (By.CSS_SELECTOR,"a.ico-register")
    EMAIL_INPUT = (By.ID,"Email")
    PASSWORD_INPUT = (By.ID,"Password")
    PASSWORD_INPUT_CONFIRM = (By.ID,"ConfirmPassword")
    BUTTON_REGISTRATION = (By.ID,"register-button")
    SIGN_OUT_BUTTON = (By.CSS_SELECTOR, "a[href='/logout']")
    GENDERS = {
        "male": (By.ID, "gender-male"),
        "female": (By.ID, "gender-female"),
    }
    FIRST_NAME = (By.ID,"FirstName")
    SEC_NAME = (By.ID,"LastName")


    def __init__(self,driver):
        self.driver = driver

    def open_registration_page(self):
        self.driver.find_element(*self.REGISTRATION_LINK).click()

    def fill_email_field(self, email):
        self.driver.find_element(*self.EMAIL_INPUT).clear()
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

    def fill_password_field(self, password):
        self.driver.find_element(*self.PASSWORD_INPUT).clear()
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def fill_password_confirmation_field(self,password_confirmation):
        self.driver.find_element(*self.PASSWORD_INPUT_CONFIRM).clear()
        self.driver.find_element(*self.PASSWORD_INPUT_CONFIRM).send_keys(password_confirmation)

    def select_gender(self, gender):
        locator = self.GENDERS.get(gender.lower())
        # if locator is None:
        #     raise ValueError(f"Unknown gender: {gender!r}")
        self.driver.find_element(*locator).click()

    def fill_first_name(self, first_name):
        self.driver.find_element(*self.FIRST_NAME).clear()
        self.driver.find_element(*self.FIRST_NAME).send_keys(first_name)

    def fill_sec_name(self, sec_name):
        self.driver.find_element(*self.SEC_NAME).clear()
        self.driver.find_element(*self.SEC_NAME).send_keys(sec_name)

    def click_on_registration_button(self):
        self.driver.find_element(*self.BUTTON_REGISTRATION).click()

    def is_sign_out_displayed(self):
        try:
            WebDriverWait(self.driver, timeout=5).until(
                expected_conditions.visibility_of_element_located(self.SIGN_OUT_BUTTON))
            return True
        except TimeoutException:
            return False

    def get_alert_text(self):
        alert = WebDriverWait(self.driver, timeout=5).until(
            expected_conditions.alert_is_present()
        )
        return alert.text

    def accept_alert(self):
        self.driver.switch_to.alert.accept()