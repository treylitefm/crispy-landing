from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.proxy import *
from browsermobproxy import Server
from datetime import datetime
import json
import os
import re
import requests

VALID_STATUS_CODES = (200, 301, 302) 
INVALID_STATUS_CODES = (404, 500)
VALID_URL_REGEX = r'^(https?:\/\/.*)'
UPSTREAM = 'http://hermes:8000/'

HOSTNAME = os.environ['HOSTNAME']

STATUSES = {
    'queued': 0,        
    'in_progress': 1,        
    'pass': 2,        
    'fail': 3,        
    'error': 4,        
}

def valid_url(url):
    if re.search(VALID_URL_REGEX, url):
        return True

def scan_script(url, browser=None, test_id=None):
    if not valid_url(url):
        # UPDATE TO INVALID_URL
        print 'Reporting status to upstream'
        requests.post(UPSTREAM+'tests/update/'+test_id+'/', data={'browser': browser, 'test_id': test_id, 'status': STATUSES['error']})
        return False 
    browsers = {
        'firefox': DesiredCapabilities.FIREFOX,
        'chrome': DesiredCapabilities.CHROME
    }

    if browser not in ('firefox', 'chrome'):
        browser = 'firefox'
    '''
    server = Server('./browsermob-proxy/bin/browsermob-proxy')

    server.start()
    proxy = server.create_proxy()
    proxy.remap_hosts('localhost', 'f8d70c279eb9')
    selenium_proxy = proxy.selenium_proxy()
    selenium_proxy.add_to_capabilities(DesiredCapabilities.FIREFOX)
    '''
    print 'Reporting status to upstream'
    requests.post(UPSTREAM+'tests/update/'+test_id+'/', data={'browser': browser, 'test_id': test_id, 'status': STATUSES['in_progress']})
    driver = webdriver.Remote(
        command_executor='http://hermes_hub_1:4444/wd/hub',
        desired_capabilities=browsers[browser]
    )

    #proxy.new_har('KAMAU', {'captureHeaders': True})
    driver.get(url)

    print 'Sleeping...'
    import time; time.sleep(2) #TODO: DUH-LETE
    print 'Done sleeping'
    
    png = 'screenshot-'+str(datetime.now())+'.png'
    png = png.replace(' ', '_')
    directory = './static/img/'
    filename = directory+png

    if not os.path.exists(directory):
        print 'Warning! Path: ./static/img/ does not exist -- Creating it now'
        os.makedirs(directory)

    print 'Attempting to save screenshot:',filename
    if driver.save_screenshot(filename):
        print 'Screenshot saved:',filename


    #with open('yo.txt', 'w') as outfile:
    #    json.dump(proxy.har, outfile)

    #server.stop()

    driver.quit()
    print 'Reporting status to upstream'
    requests.post(UPSTREAM+'tests/update/'+test_id+'/', data={'screenshot': png, 'browser': browser, 'test_id': test_id, 'status': STATUSES['pass']})

'''
if __name__ == '__main__':
    #main('http://192.168.99.100:5000')
    #main('https://google.com')
'''

