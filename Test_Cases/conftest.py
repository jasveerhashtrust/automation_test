import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

# Specify the path to the ChromeDriver executable on your system
chrome_driver_path = '/usr/local/bin/chrome-linux64'

# Start the ChromeDriver service
service = ChromeService(executable_path=chrome_driver_path)
service.start()

# Configure ChromeDriver options, such as running in headless mode
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')

# Initialize the WebDriver with the service and options
driver = webdriver.Chrome(service=service, options=chrome_options)

# Fixture for setting up the driver


@pytest.fixture(scope="class")
def setup(request):
    driver.get('https://fetch.ai/docs/guides/agents/create-a-uagent')
    driver.maximize_window()
    time.sleep(2)
    yield
    driver.quit()
