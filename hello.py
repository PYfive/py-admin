from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'index page'


@app.route('/login', methods=['POST'])
def login():
    return 'hello page'
