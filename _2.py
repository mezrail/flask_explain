from flask import Flask, render_template

app = Flask(__name__)

#127.0.0.1:5000
@app.route('/')
def index():
    return "<h1>hello world</h1>"

#127.0.0.1:5000/user/jhon
@app.route('/user/<name>')
def user(name):
    return "<h1>hello {}</h1>".format(name)

#export FLASK_APP=_2.py calistiracagin file i goster bash te
#browserda yaz  :  http://127.0.0.1:5000/user/emine