from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from browsermobproxy import Server
from uptool import get_http_status_code
from datetime import datetime
import json
import re

VALID_STATUS_CODES = (200, 301, 302) 
INVALID_STATUS_CODES = (404, 500)

VALID_URL_REGEX = r'^(https?:\/\/.*)'

def parse_link(css_background_property):
    m = re.search(r'\(\"(.*)\"\)', css_background_property)
    if m:
        return m.group(1)

def valid_url(url):
    if re.search(VALID_URL_REGEX, url):
        return True

def scan_script(url):
    #driver = webdriver.Firefox()
    driver = webdriver.Remote(
        command_executor='http://docker-dev:4444/wd/hub',
        desired_capabilities=DesiredCapabilities.FIREFOX
    )
    driver.maximize_window()
    driver.get(url)

    print 'Sleeping...'
    import time; time.sleep(2) #TODO: DUH-LETE
    print 'Done sleeping'

    filename = './static/img/screenshot-'+str(datetime.now())+'.png'
    print filename,type(filename)
    if driver.save_screenshot(filename):
        print 'Screenshot saved:',filename

    driver.quit()

'''
server = Server('./bin/browsermob-proxy')
server.start()
proxy = server.create_proxy()

profile = webdriver.FirefoxProfile()
profile.set_proxy(proxy.selenium_proxy())

driver = webdriver.Firefox(firefox_profile=profile)

#proxy_new_har(file_name)

driver.get(url)

#with open('yo.txt', 'w') as outfile:
#    json.dump(proxy.har, outfile)

def test_loaded(driver):
    for status_code in status_codes:
        assert status_code in VALID_STATUS_CODES
def test_links_images(driver):
    pass
def take_screenshot():
    pass

server.stop()
driver.quit()
'''
