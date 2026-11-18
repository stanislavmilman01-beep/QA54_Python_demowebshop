from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    TIME_OUT: int = 10

    def __init__(self, driver):
        self.driver = driver

    def fill_text_input(self, locator, text):
        email_input = self.driver.find_element(*locator)
        email_input.clear()
        email_input.send_keys(text)

    def click(self, locator):
        self.driver.find_element(*locator).click()

    def is_element_shown(self, locator):
        try:
            WebDriverWait(self.driver, self.TIME_OUT).until(
                expected_conditions.visibility_of_element_located(locator)
            )

            return True
        except TimeoutException:
            return False

    def is_page_redirected(self, partial_url) -> bool:
        try:
            WebDriverWait(self.driver, self.TIME_OUT).until(
                expected_conditions.url_contains(partial_url)
            )

            return True
        except TimeoutException:
            return False

    def get_element_text(self, locator) -> str | None:
        try:
            element = WebDriverWait(self.driver, self.TIME_OUT).until(
                expected_conditions.visibility_of_element_located(locator)
            )

            return element.text
        except TimeoutException:
            return None

    def clear(self):
        self.driver.delete_all_cookies()
