from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
    wait = WebDriverWait(driver, 10)

    start_btn = wait.until(EC.element_to_be_clickable((
        By.XPATH, "//button[text()='Start']")))
    start_btn.click()

    wait.until(EC.text_to_be_present_in_element((
        By.ID, "finish"), "Hello World!"))

    driver.save_screenshot("lesson_06/screenshots/full_page.png")

    hello_element = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//h4[text()='Hello World!']")))

    assert hello_element.is_displayed(), (
        "Элемент с текстом 'Hello World!' не отображается")
    assert hello_element.text == "Hello World!", (
        f"Текст элемента не 'Hello World!', а '{hello_element.text}'")
    text_via_js = driver.execute_script(
        "return arguments[0].textContent;", hello_element)
    assert text_via_js == "Hello World!", (
        f"Текст через JavaScript не 'Hello World!', а '{text_via_js}'")

    assert hello_element.is_displayed(), "Элемент не видим на странице"

    driver.quit()
