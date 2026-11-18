from selenium.webdriver.common.by import By


class ShoppingPage:

    BASE_PAGE = (By.CSS_SELECTOR,"[alt='Tricentis Demo Web Shop']")
    ADD_TO_CART = (By.XPATH,"(//input[@value='Add to cart'])[2]")
    SHOP_CART = (By.CSS_SELECTOR,"[class='cart-label']")
    QTY_IN_CART = (By.XPATH,"//input[contains(@class, 'qty-input')]")

    def __init__(self,driver):
        self.driver = driver

    def click_page_button(self):
        self.driver.find_element(*self.BASE_PAGE).click()

    def click_add_to_cart(self):
        self.driver.find_element(*self.ADD_TO_CART).click()

    def open_shop_cart(self):
        self.driver.find_element(*self.SHOP_CART).click()

    def add_success(self):
        return self.driver.find_element(*self.QTY_IN_CART).get_attribute("value")



