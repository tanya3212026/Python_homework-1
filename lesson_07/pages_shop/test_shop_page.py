from lesson_07.pages_shop.login_page import LoginPage
from lesson_07.pages_shop.main_page import MainPage
from lesson_07.pages_shop.cart_page import CartPage
from lesson_07.pages_shop.checkout_page import CheckoutPage


def test_shop_checkout_flow(driver_firefox):
    login_page = LoginPage(driver_firefox)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    main_page = MainPage(driver_firefox)
    products = [
        "sauce-labs-backpack",
        "sauce-labs-bolt-t-shirt",
        "sauce-labs-onesie"
    ]
    for product in products:
        main_page.add_product_to_cart(product)

    main_page.go_to_cart()

    cart_page = CartPage(driver_firefox)
    cart_page.click_checkout()

    checkout_page = CheckoutPage(driver_firefox)
    checkout_page.fill_form("Петр", "Сидоров", "143416")

    total = checkout_page.get_total()
    assert total == "Total: $58.29", f"Ожидалось $58.29, получено {total}"
