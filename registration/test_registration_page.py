from registration.registration_page import RegistrationPage
import time

VALID_EMAIL = f"qa_{int(time.time())}@test.com"
VALID_PASSWORD = "1234Qwerty!"
VALID_PASSWORD_CONFIRM = "1234Qwerty!"
GENDER = "male"
FIRST_NAME = "Stas"
SEC_NAME = "Milman"


def test_valid_registration_success(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open_registration_page()

    registration_page.select_gender(GENDER)
    registration_page.fill_first_name(FIRST_NAME)
    registration_page.fill_sec_name(SEC_NAME)
    registration_page.fill_email_field(VALID_EMAIL)
    registration_page.fill_password_field(VALID_PASSWORD)
    registration_page.fill_password_confirmation_field(VALID_PASSWORD_CONFIRM)

    registration_page.click_on_registration_button()

    assert registration_page.is_sign_out_displayed()







