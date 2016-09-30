from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from rq import Queue
from redis import Redis
from page_scan import scan_script
import json

import time

app = Flask(__name__)
app.secret_key = '6cc5dc1943546a5fd372b7795692f2f2eeae5cb285566949'
REDIS_HOST = 'redis-server'

q = Queue(connection=Redis(REDIS_HOST))


@app.route('/')
def index():
    return jsonify(message='Hello World!', success=None)

@app.route('/launch/', methods=['POST'])
def launch():
    message = 'Launching test (hopefully)!'
    success = False

    if 'test_id' not in request.form:
        message = 'Test ID not specified'
        return jsonify(message=message, success=success)

    if 'browser' not in request.form:
        browser = 'firefox'
    else:
        browser = request.form['browser']

    if 'url' in request.form:
        if type(request.form['url']) is list:
            for link in request.form['url']:
                q.enqueue(scan_script, link, browser, request.form['test_id'])
        else:
            q.enqueue(scan_script, request.form['url'], browser, request.form['test_id'])

        success = True
    
    return jsonify(message=message, success=success)


app.run(debug=True, host='0.0.0.0', port=6000)
