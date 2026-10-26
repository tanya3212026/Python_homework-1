from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_01_form():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    fields = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro",
    }

    for name, value in fields.items():
        field = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, f'input[name="{name}"]')))
        field.send_keys(value)

    zip_input = driver.find_element(By.CSS_SELECTOR, 'input[name="zip-code"]')
    zip_input.clear()

    wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "button.btn.btn-outline-primary.mt-3"))).click()

    zip_result = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "#zip-code.alert-danger")))
    assert "alert-danger" in zip_result.get_attribute("class"), \
        "Zip code не красный"

    green_fields = wait.until(EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, ".alert-success")))
    assert len(green_fields) == 9, f"Ожидалось 9 зелёных, \
        найдено {len(green_fields)}"

    driver.quit()
