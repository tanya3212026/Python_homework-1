from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()
# открыть страницу https://httpbin.qa-territory.online/
    driver.get("https://httpbin.qa-territory.online/")
# Запоминаем исходный URL
    original_url = driver.current_url
# кликнуть на ссылку HTML Form
    driver.find_element(By.LINK_TEXT, "HTML Form").click()
# Проверить, что URL изменился на /forms/post
    assert "/forms/post" in driver.current_url
# Вернуться назад на главную страницу
    driver.back()
# Проверить, что вернулась на исходный URL.
    assert driver.current_url == original_url

    driver.quit()
