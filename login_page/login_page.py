from selenium.webdriver.common.by import By

from login_page.base_page import BasePage


class LoginPage(BasePage):
    URL: str = "https://demowebshop.tricentis.com/login"

    EMAIL_INPUT: tuple[str, str] = (By.ID, "Email")
    PASSWORD_INPUT: tuple[str, str] = (By.ID, "Password")
    REMEMBER_ME_BOX: tuple[str, str] = (By.ID, "RememberMe")
    LOGIN_BUTTON: tuple[str, str] = (By.CSS_SELECTOR, "[type='submit'][value='Log in']")
    ACCOUNT_LINK: tuple[str, str] = (By.CSS_SELECTOR, "div.header a[href='/customer/info']")

    LOGIN_ERROR: tuple[str, str] = (By.XPATH, "//span[contains(text(), 'Login was unsuccessful')]")
    EMAIL_ERROR: tuple[str, str] = (By.XPATH, "//span[text()='Please enter a valid email address.']")
    PASSWORD_ERROR: tuple[str, str] = (By.XPATH, "//li[contains(text(), 'credentials provided are incorrect')]")
    NO_CUSTOMER_ERROR: tuple[str, str] = (By.XPATH, "//li[contains(text(), 'No customer account')]")


    def load(self):
        self.driver.get(self.URL)

    def fill_email_input(self, email):
        self.fill_text_input(self.EMAIL_INPUT, email)

    def fill_password_input(self, password):
        self.fill_text_input(self.PASSWORD_INPUT, password)

    def click_login_button(self):
        self.click(self.LOGIN_BUTTON)

    def check_remember_me(self):
        self.click(self.REMEMBER_ME_BOX)

    def log_in(self, email, password):
        self.fill_email_input(email)
        self.fill_password_input(password)
        self.click_login_button()

    def get_account_link_text(self) -> str | None:
        return self.get_element_text(self.ACCOUNT_LINK)

    def is_email_error_shown(self):
        return self.is_element_shown(self.EMAIL_ERROR)

    def is_password_error_shown(self):
        return self.is_element_shown(self.PASSWORD_ERROR)

    def is_login_error_shown(self):
        return self.is_element_shown(self.LOGIN_ERROR)

    def is_no_customer_error_shown(self):
        return self.is_element_shown(self.NO_CUSTOMER_ERROR)
