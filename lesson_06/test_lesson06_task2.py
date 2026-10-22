from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_session_storage_auth():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    cookie_user1 = ({
        "name": "SESSION",
        "value": "MDMwZjI5NzUtZGVkZC00YjJlLTk4NWUtYTIzZjAxODdmNzFk",
        "domain": "gitflic.ru"
        })
    cookie_user2 = ({
        "name": "SESSION",
        "value": "MWYxODg2NzctN2UwNy00OTZkLWI5YjUtODA3MjAyNDM1NTlh",
        "domain": "gitflic.ru"
        })

    driver.get("https://gitflic.ru/")

    driver.add_cookie(cookie_user1)

    driver.refresh()

    driver.get("https://gitflic.ru/project?sort=updated_at&direction=ASC")

    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    url_user1 = driver.current_url

    driver.delete_all_cookies()

    driver.refresh()

    driver.add_cookie(cookie_user2)

    driver.refresh()

    driver.get(
        "https://gitflic.ru/project?sort=updated_at&direction=ASC&continue")

    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    url_user2 = driver.current_url

    assert url_user1 != url_user2, (
        f"URL пользователей совпадают! URL1: {url_user1}, URL2: {url_user2}"
    )

    driver.quit()
