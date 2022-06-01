import os

import requests
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


def discord_notify_setup():
    if os.name == 'posix':
        if os.path.isfile("discord.sh"):
            return True
        else:
            try:
                print("SETUP : 'discord.sh' script is not present. Downloading...")
                filename = "discord.sh"
                url = 'https://raw.githubusercontent.com/ChaoticWeg/discord.sh/master/discord.sh'
                f = requests.get(url)
                open(filename, 'wb').write(f.content)
                os.popen('chmod +x discord.sh').read()
                print("SETUP : 'discord.sh' script downloaded.")
                return True
            except Exception as e:
                print(f"ERROR : Something went wrong while downloadind script. Msg: {e}")
    else:
        print(f'INFO : Discord notification will work only on Unix system. System now is "{os.name}"')
