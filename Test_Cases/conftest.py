import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="class")
def setup(request):
    # global driver

    service = Service(
        executable_path="/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/selenium/webdriver/chrome/webdriver.py")
    driver = webdriver.Chrome(service=service)
    driver.get('https://fetch.ai/docs/guides/agents/create-a-uagent')
    driver.maximize_window()
    time.sleep(2)
    # yield
    # driver.quit()
    # request.cls.driver = webdriver.Chrome()
    # request.cls.driver.get(
    #     'https://fetch.ai/docs/guides/agents/create-a-uagent')
    # request.cls.driver.maximize_window()
    # time.sleep(2)
    # yield
    # request.cls.driver.quit()
