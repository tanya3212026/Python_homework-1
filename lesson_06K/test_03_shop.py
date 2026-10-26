from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_03_shop():
    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    products = [
        "sauce-labs-backpack",
        "sauce-labs-bolt-t-shirt",
        "sauce-labs-onesie"
    ]
    for product in products:
        button = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, f"button[name='add-to-cart-{product}']")))
        button.click()

    wait.until(EC.element_to_be_clickable(
            (By.CLASS_NAME, "shopping_cart_link"))).click()

    wait.until(EC.element_to_be_clickable(
            (By.ID, "checkout"))).click()

    wait.until(EC.presence_of_element_located(
            (By.ID, "first-name"))).send_keys("Петр")
    driver.find_element(By.ID, "last-name").send_keys("Сидоров")
    driver.find_element(By.ID, "postal-code").send_keys("143416")

    driver.find_element(By.ID, "continue").click()

    total = wait.until(EC.presence_of_element_located(
        (By.CLASS_NAME, "summary_total_label"))).text

    assert total == "Total: $58.29", f"Ожидалось $58.29, получено {total}"

    driver.quit()
