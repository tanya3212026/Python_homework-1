from selenium import webdriver
from selenium.webdriver.common.by import By


# Открыть страницу https://httpbin.qa-territory.online/forms/post.
def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/forms/post")
# Запомнить исходный URL
    original_url = driver.current_url
# Найти поле ввода с названием custname.
    name_input = driver.find_element(By.NAME, "custname")
# Ввести в него моё имя.
    name_input.send_keys("Татьяна")
# Найти кнопку Submit и нажать на нее.
    submit_button = driver.find_element(
        By.XPATH,
        "//button[contains(text(), 'Submit')]")
    submit_button.click()
# Проверить, что после нажатия URL изменился.
    assert driver.current_url != original_url

    driver.quit()
