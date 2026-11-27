# Lesson 10: Автоматизация тестирования калькулятора с Allure

## Описание проекта
Проект содержит UI-тесты для проверки работы калькулятора (slow-calculator).
Используются: Python, Selenium WebDriver, Pytest, Allure для формирования отчетов.

## Базовый синтаксис и форматирование
*   **Python** — основной язык.
*   **Selenium** — библиотека для автоматизации браузера.
*   **Pytest** — фреймворк для тестирования.
*   **Allure** — инструмент для отчетов.
*   Код оформлен в соответствии с **PEP 8** (стандарт написания кода на Python).
*   Все методы классов содержат docstrings (описание) и типизацию (Type Hints).
*   Шаги тестов размечены декораторами `@allure.step` и `with allure.step`.

## Инструкция по запуску тестов и формированию отчета
1.  Установите необходимые зависимости:
    ```bash
    pip install -r requirements.txt

2. Запустите тесты и сохраните сырые данные для Allure в папку `allure-results`:
   ```bash
   pytest test_calculator.py --alluredir=allure-results

3.  Сгенерируйте красивый HTML-отчет в папку `final-report`:
    ```bash
    allure generate allure-results -o final-report --clean

## Инструкция по просмотру сформированного отчета
4.  Откройте сгенерированный отчет в браузере
    ```bash
    allure open final-report  

 