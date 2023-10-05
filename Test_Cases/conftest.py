import time
import pytest
from selenium import webdriver
# driver = None
import shutil

options = webdriver.ChromeOptions()
options.add_argument('--headless')

# Search for the Chrome binary in common locations
chrome_binary = shutil.which(
    'google-chrome') or shutil.which('chromium-browser')

if chrome_binary:
    options.binary_location = chrome_binary
    driver = webdriver.Chrome(options=options)
else:
    raise Exception("Chrome binary not found. Please specify the path.")


@pytest.fixture(scope="class")
def setup(request):
    # global driver
    request.cls.driver = webdriver.Chrome()
    request.cls.driver.get(
        'https://fetch.ai/docs/guides/agents/create-a-uagent')
    request.cls.driver.maximize_window()
    time.sleep(2)
    yield
    request.cls.driver.quit()
