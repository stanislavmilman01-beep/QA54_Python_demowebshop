from shopping_cart.shopping_page import ShoppingPage


def test_adding_success(driver):

    shopping_page = ShoppingPage(driver)
    shopping_page.click_page_button()
    shopping_page.click_add_to_cart()
    shopping_page.open_shop_cart()

    assert shopping_page.add_success() > "0"