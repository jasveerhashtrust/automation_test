import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import undetected_chromedriver.v2 as uc


# Specify the path to the ChromeDriver executable on your system
chrome_driver_path = '/usr/local/bin/chrome-linux64'

# Check and adjust file permissions if needed
if not os.access(chrome_driver_path, os.X_OK):
    os.chmod(chrome_driver_path, 0o755)  # Give execute permissions (755)

# Start the ChromeDriver service
service = ChromeService(executable_path=chrome_driver_path)
service.start()

# Configure ChromeDriver options, such as running in headless mode
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')

# Initialize the WebDriver with the service and options
chrome_options = uc.ChromeOptions()
driver = webdriver.Chrome(service=service, options=chrome_options)

# Fixture for setting up the driver


@pytest.fixture(scope="class")
def setup(request):
    driver.get('https://fetch.ai/docs/guides/agents/create-a-uagent')
    driver.maximize_window()
    time.sleep(2)
    yield
    driver.quit()
