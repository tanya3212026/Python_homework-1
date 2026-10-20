from selenium import webdriver
from selenium.webdriver.common.by import By


# Открыть страницу https://httpbin.qa-territory.online/links/10.
def test_multiple_elements():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/links/10")
# Найти все ссылки на странице (тег <a>).
    links = driver.find_elements(By.TAG_NAME, "a")
# Проверить, что количество ссылок равно 9.
    assert len(links) == 9, f"Ожидалось 9 ссылок, найдено {len(links)}"
# Проверить, что все ссылки отображаются на странице.
    for link in links:
        assert link.is_displayed(), f"Ссылка {link.text} не отображается"
# Проверить, что текст первой ссылки содержит "1".
    assert "1" in links[0].text, f"Текст первой ссылки: {links[0].text}"

    driver.quit()
