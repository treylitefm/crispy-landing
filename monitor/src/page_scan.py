from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.proxy import *
from browsermobproxy import Server
from datetime import datetime
import json
import re

VALID_STATUS_CODES = (200, 301, 302) 
INVALID_STATUS_CODES = (404, 500)

VALID_URL_REGEX = r'^(https?:\/\/.*)'

def valid_url(url):
    if re.search(VALID_URL_REGEX, url):
        return True

#def scan_script(url):
def main(url):
    server = Server('./browsermob-proxy/bin/browsermob-proxy')
    server.start()
    proxy = server.create_proxy()

    DesiredCapabilities.FIREFOX['proxy'] = {
        'httpProxy': proxy.host,
        'ftpProxy': proxy.host,
        'sslProxy': proxy.host,
        'noProxy': None,
        'proxyType': 'MANUAL',
        'class': 'org.openqa.selenium.Proxy',
        'autodetext': False,
    }

    driver = webdriver.Remote(
        command_executor='http://hermes_hub_1:4444/wd/hub',
        desired_capabilities=DesiredCapabilities.FIREFOX
    )

    driver.maximize_window()
    proxy.new_har('KAMAU')
    driver.get(url)

    print 'Sleeping...'
    import time; time.sleep(2) #TODO: DUH-LETE
    print 'Done sleeping'

    filename = './static/img/screenshot-'+str(datetime.now())+'.png'
    filename = filename.replace(' ', '_')
    print 'Attempting to save screenshot:',filename
    if driver.save_screenshot(filename):
        print 'Screenshot saved:',filename


    with open('yo.txt', 'w') as outfile:
        json.dump(proxy.har, outfile)

    server.stop()
    driver.quit()

if __name__ == '__main__':
    #main('http://192.168.99.100:5000')
    main('https://google.com')
