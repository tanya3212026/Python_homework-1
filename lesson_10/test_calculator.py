import allure
import pytest
from selenium import webdriver
from lesson_10.calc_page import CalcPage


@pytest.fixture()
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера.
    """
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.feature("Калькулятор")
@allure.story("Арифметические операции")
@allure.title("Тестирование калькулятора:"
              "{num1} {operation} {num2} = {expected}")
@allure.description("Тест проверяет работу калькулятора с задержкой.")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize(
    "num1, operation, num2, expected, delay",
    [
        ("7", "+", "8", "15", 45),
        ("9", "-", "3", "6", 10),
        ("4", "x", "5", "20", 20),
        ("8", "÷", "2", "4", 5),
    ],
)
def test_calculator_with_delay(driver, num1, operation, num2, expected, delay):
    """
    Тест проверяет работу калькулятора с различными операциями.

    :param driver: WebDriver — объект драйвера.
    :param num1: str — первое число.
    :param operation: str — операция (+, -, x, ÷).
    :param num2: str — второе число.
    :param expected: str — ожидаемый результат.
    :param delay: int — задержка в секундах.
    """
    calc_page = CalcPage(driver)

    with allure.step("Открытие страницы калькулятора"):
        calc_page.open()

    with allure.step(f"Установка задержки {delay} секунд"):
        calc_page.set_delay(delay)

    with allure.step(f"Нажатие кнопок: {num1}, {operation}, {num2}, '='"):
        calc_page.click_button(num1)
        calc_page.click_button(operation)
        calc_page.click_button(num2)
        calc_page.click_button("=")

    with allure.step(f"Проверка результата: ожидаем {expected}"):
        result = calc_page.get_screen_result(expected)
        assert result == expected, \
            f"Ожидали {expected}, но получили: {result}"
