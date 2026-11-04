from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:
    DELAY_INPUT = (By.CSS_SELECTOR, "#delay")
    SCREEN = (By.CSS_SELECTOR, ".screen")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

    def open(self):
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator."
            "html")

    def set_delay(self, seconds):
        delay_field = self.wait.until(
            EC.presence_of_element_located(self.DELAY_INPUT))
        delay_field.clear()
        delay_field.send_keys(str(seconds))

    def click_button(self, button_text):
        xpath = f"//span[text()='{button_text}']"
        self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath))).click()

    def get_screen_result(self):
        self.wait.until(EC.text_to_be_present_in_element(self.SCREEN, "15"))
        return self.driver.find_element(*self.SCREEN).text
