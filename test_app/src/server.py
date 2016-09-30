from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = '\xad\x8b\xb4A\xdcGv\xb9P%\xf9B1\xbb\xc3\xd9\x1ff\x94K&6:\xde'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninjas')
def ninjas():
    return render_template('index.html', all_ninjas=True)

@app.route('/ninjas/<ninja_color>')
def ninja(ninja_color):
    if ninja_color in ['blue', 'orange', 'red', 'purple']:
        return render_template('index.html', ninja=ninja_color)
    else:
        return render_template('index.html', ninja='april')

app.run(debug=True, host='0.0.0.0')
