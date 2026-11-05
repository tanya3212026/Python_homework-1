from lesson_07.CalcPages.calc_page import CalcPage


def test_calculator_with_delay(driver):
    calc_page = CalcPage(driver)
    calc_page.open()
    calc_page.set_delay(45)
    calc_page.click_button("7")
    calc_page.click_button("+")
    calc_page.click_button("8")
    calc_page.click_button("=")

    result = calc_page.get_screen_result()

    assert result == "15", f"Ожидали 15, но получили: {result}"
