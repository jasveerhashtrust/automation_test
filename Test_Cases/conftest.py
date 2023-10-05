import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


from selenium.webdriver.chrome.service import Service as ChromeService

service = ChromeService(executable_path='/path/to/chromedriver')
service.start()
options = webdriver.ChromeOptions()
# Optional, if you want to run tests headlessly
options.add_argument('--headless')
driver = webdriver.Chrome(service=service, options=options)


@pytest.fixture(scope="class")
def setup(request):
    # global driver
    service = ChromeService(executable_path='usr/local/bin/chrome-linux64')
    service.start()
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(
        'https://fetch.ai/docs/guides/agents/create-a-uagent')
    driver.maximize_window()
    time.sleep(2)
    yield
    driver.quit()
