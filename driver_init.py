from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


class SeleniumDriver:
    def __init__(self):
        self.options = Options()
        self.options.add_argument("--headless")
        self.options.add_argument('--no-sandbox')
        self.options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.options)

    def get_driver(self):
        return self.driver

    def close_driver(self):
        self.driver.quit()
