# Ran using Python -version: 3.6.4.  Full Stack trace in the README.md
# This results in NO VM session.  The below stacktrace error is returned in the terminal:
# selenium.common.exceptions.WebDriverException: Message: No browserName or device specified in session request. Please check our platforms documentation (https://saucelabs.com/docs/platforms): {'goog:chromeOptions': {'w3c': 'true'}, 'sauce:platform': 'Windows 10', 'sauce:browserVersion': '65', 'sauce:seleniumVersion': '3.8.0', 'sauce:browserName': 'chrome'}
# - Max Dobeck
from selenium import webdriver
from sauceclient import SauceClient
import os

username = os.environ.get('SAUCE_USERNAME')
access_key = os.environ.get('SAUCE_ACCESS_KEY')
sauce_client = SauceClient(username, access_key)

desired_caps = {
    'sauce:platform': "Windows 10",
    'sauce:browserName': "chrome",
    'sauce:browserVersion': "65",
    'sauce:seleniumVersion': "3.9.1",
    'goog:chromeOptions':{"w3c": "true"}
}

driver = webdriver.Remote(command_executor="https://%s:%s@ondemand.saucelabs.com/wd/hub" % (username, access_key), desired_capabilities=desired_caps)
driver.implicitly_wait(30)
driver.maximize_window()
driver.get("https://www.google.com")

sauce_client.jobs.update_job(driver.session_id, passed=True)

driver.quit()
