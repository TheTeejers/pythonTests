# Good example of how to start RDC Test
# Max Dobeck

from appium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from appium.webdriver.common.touch_action import TouchAction
import time, os

# device = "iphone [78]||iphone xs||iphone x"
device = "iPhone X.*|iPhone [78].*|iPad Pro 9.7|iPadAir21|iPadmini41|iPad Pro .*"
# device = "iphone 7|iphone 8"

desired_capabilities = {}
desired_capabilities['testobject_api_key'] = os.environ['my_project_KEY']
desired_capabilities['platformName'] = 'iOS'
desired_capabilities['name'] = "DeviceName - " + device
#desired_capabilities['platformVersion'] = '8' 
desired_capabilities['deviceName'] = device

EU_endpoint = 'http://eu1.appium.testobject.com/wd/hub'
US_endpoint = 'http://us1.appium.testobject.com/wd/hub'

# The driver will take care of establishing the connection, so we must provide
# it with the correct endpoint and the requested capabilities.
try:
    driver = webdriver.Remote(US_endpoint, desired_capabilities)
    print("\n\nTest", driver.capabilities['name'], " obtained device: ", driver.capabilities['testobject_device_name'])
    print("Link to full Test here: ", driver.capabilities['testobject_test_report_url'])
    # print("DeviceName Cap: ", device)
    # print(driver.session_id)
    # print(driver.desired_capabilities)
    driver.get("https://www.saucedemo.com/")
    # print(driver.page_source)
    time.sleep(6)
except Exception as e:
    print("Something went wrong >>>>>>>>>>>>>>>", e)
    exit(1)
driver.quit()
