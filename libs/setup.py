from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def __init__(self):
    self.driver = None


def set_up(website):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--no-sandbox --profile-directory=Default')
    # s = Service('drivers/chromedriver')
    s = Service(ChromeDriverManager().install())
    # chrome_options.add_argument("--profile-directory=Default")
    driver = webdriver.Chrome(service=s, options=chrome_options)
    driver.implicitly_wait(10)
    driver.get(website)
    return driver
