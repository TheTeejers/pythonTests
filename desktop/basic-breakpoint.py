# Basic test with an optional w3c capability for chrome
from selenium import webdriver
from sauceclient import SauceClient
import time
import os

username = os.environ.get('SAUCE_USERNAME')
access_key = os.environ.get('SAUCE_ACCESS_KEY')
sauce_client = SauceClient(username, access_key)

desired_caps = {
    'platform': "Windows 10",
    'browserName': "chrome",
    'version': "65.0",
    'seleniumVersion': "3.9.1",
    'name': "My Python Breakpoint Test"
}

driver = webdriver.Remote(command_executor="https://%s:%s@ondemand.saucelabs.com/wd/hub" % (username, access_key), desired_capabilities=desired_caps)
time.sleep(3)
driver.maximize_window()
driver.get("https://saucelabs.com")
driver.execute_script("sauce: break")
sauce_client.jobs.update_job(driver.session_id, passed=True)

driver.quit()
