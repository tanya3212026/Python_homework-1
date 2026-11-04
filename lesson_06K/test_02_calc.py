from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_02_calc():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    delay_input = wait.until(EC.presence_of_element_located(
      (By.CSS_SELECTOR, "#delay")))
    delay_input.clear()
    delay_input.send_keys("45")

    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//span[text()='7']"))).click()
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//span[text()='+']"))).click()
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//span[text()='8']"))).click()
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//span[text()='=']"))).click()

    result_wait = WebDriverWait(driver, 60)
    result = result_wait.until(EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, ".screen"), "15"))

    assert result, "Результат 15 не отобразился за отведённое время"

    driver.quit()
