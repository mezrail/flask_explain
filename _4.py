from flask import Flask, render_template

app = Flask(__name__)

#127.0.0.1:5000
@app.route('/')
def index():
    first_name = "ilker"
    favorite_pizza = ['pepperoni', 'cheese', 'mushrooms']
    return render_template('index2.html', first_name=first_name, favorite_pizza=favorite_pizza)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500
#export FLASK_APP=_4.py calistiracagin file i goster bash te
#flask run yaz bash te
#browserda yaz  :  http://127.0.0.1:5000