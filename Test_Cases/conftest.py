from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time
import pytest
import chromedriver_autoinstaller
from pyvirtualdisplay import Display
display = Display(visible=0, size=(800, 800))
display.start()

# Check if the current version of chromedriver exists
chromedriver_autoinstaller.install()
# and if it doesn't exist, download it automatically,
# then add chromedriver to path

chrome_options = webdriver.ChromeOptions()
# Add your options as needed
options = [
    # Define window size here
    "--window-size=1200,1200",
    "--ignore-certificate-errors"

    # "--headless",
    # "--disable-gpu",
    # "--window-size=1920,1200",
    # "--ignore-certificate-errors",
    # "--disable-extensions",
    # "--no-sandbox",
    # "--disable-dev-shm-usage",
    # '--remote-debugging-port=9222'
]

for option in options:
    chrome_options.add_argument(option)


@pytest.fixture(scope="class")
def setup(request):
    request.cls.driver = webdriver.Chrome(options=chrome_options)
    request.cls.driver.get(
        'https://fetch.ai/docs/guides/agents/create-a-uagent')
    request.cls.driver.maximize_window()
    time.sleep(2)
    yield
    request.cls.driver.quit()
