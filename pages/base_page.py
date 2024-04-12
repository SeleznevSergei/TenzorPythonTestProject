from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser, url=''):
        self.browser = browser
        self.url = url

    def to_site(self):
        self.browser.get(self.url)

    def get(self, url):
        self.browser.get(url)

    def get_current_url(self):
        return self.browser.current_url

    def find_element(self, locator):
        return self.browser.find_element(*locator)

    def get_array_elements(self, locator):
        return self.browser.find_elements(*locator)

    def wait_click_element(self, locator, time=10):
        return WebDriverWait(self.browser, time).until(EC.element_to_be_clickable(locator))

    def wait_text_element(self, locator, text, time=10):
        return WebDriverWait(self.browser, time).until(EC.text_to_be_present_in_element(locator, text))
