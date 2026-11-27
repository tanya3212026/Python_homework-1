import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class CalcPage:
    DELAY_INPUT = (By.CSS_SELECTOR, "#delay")
    SCREEN = (By.CSS_SELECTOR, ".screen")

    def __init__(self, driver: WebDriver) -> None:
        """
        Конструктор класса CalcPage.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

    @allure.step("Открытие страницы калькулятора")
    def open(self) -> None:
        """
        Открывает страницу калькулятора.
        """
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator."
            "html"
        )

    @allure.step("Установка задержки {seconds} секунд")
    def set_delay(self, seconds: int) -> None:
        """
        Устанавливает задержку для выполнения операций на калькуляторе.

        :param seconds: int — время задержки в секундах.
        """
        delay_field = self.wait.until(
            EC.presence_of_element_located(self.DELAY_INPUT))
        delay_field.clear()
        delay_field.send_keys(str(seconds))

    @allure.step("Нажатие кнопки '{button_text}'")
    def click_button(self, button_text: str) -> None:
        """
        Нажимает на кнопку калькулятора.

        :param button_text: str — текст на кнопке, которую нужно нажать.
        """
        xpath = f"//span[text()='{button_text}']"
        self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath))).click()

    @allure.step("Получение результата с экрана калькулятора")
    def get_screen_result(self, expected_result: str) -> str:
        """
        Ожидает появления результата и возвращает его с экрана.

        :param expected_result: str — ожидаемый результат.
        :return: str — текст результата на экране калькулятора.
        """
        self.wait.until(EC.text_to_be_present_in_element(
            self.SCREEN, expected_result))
        return self.driver.find_element(*self.SCREEN).text
