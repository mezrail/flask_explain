#templates folder oluştur FLASKER ın icinde icinde icine de index.html file olustur

from flask import Flask, render_template

app = Flask(__name__)

#127.0.0.1:5000
@app.route('/')
def index():
    first_name = "ilker"
    return render_template('index.html', first_name=first_name)

#127.0.0.1:5000/user/jhon
# @app.route('/user/<name>')
# def user(name):
#     return "<h1>hello {}</h1>".format(name)



#jinja2  kullanarak isim gecirmek sayfaya
@app.route('/user/<name>')
def user(name):
    return render_template("user.html", user_name=name)#.html in icnde user_name var jinja2 ile isaretli yani : {{}}

#export FLASK_APP=_3.py calistiracagin file i goster bash te
#flask run yaz bash te
#browserda yaz  :  http://127.0.0.1:5000

#templates folder oluştur FLASKER ın icinde icine de index.html file olustur
#jinja2 is a templating language
