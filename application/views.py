from flask import Blueprint, render_template, send_file

views = Blueprint('views', __name__)

@views.route('/')
def index():
    return send_file('index.html', mimetype='text/html')

@views.route('/home')
def home():
    return render_template('home.html')

@views.route('/data')
def data():
    return render_template('data.html')

@views.route('/favicon.ico')
def favicon():
    return '<link rel="icon" href="data:;base64,iVBORw0KGgo=">'