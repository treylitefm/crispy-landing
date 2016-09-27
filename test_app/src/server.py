from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = '6cc5dc1943546a5fd372b7795692f2f2eeae5cb285566949'

@app.route('/')
def index():
    return render_template('index.html')

app.run(debug=True, host='0.0.0.0')
