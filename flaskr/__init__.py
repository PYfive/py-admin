import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import request

# create and configure the app
app = Flask(__name__, instance_relative_config=True)

app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@localhost:3306/test_db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255), unique=True)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username


# a simple page that says hello
@app.route('/hello')
def hello():
    return 'Hello, World!'


@app.route('/login', methods=['POST'])
def login():
    objs = db.session.query(User.username, User.password)
    data = request.get_json
    return objs
