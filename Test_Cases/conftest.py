import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


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
