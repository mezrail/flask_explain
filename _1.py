#get bash terminal
#python -m venv virt
#source virt/Scripts/activate
#pip install flask

from flask import Flask, render_template

#create flask instance
app = Flask(__name__)

#create a route decorator
@app.route('/')
def index():
    return "<h1>hello world</h1>"
# run lamadan once bash terminalde  export FLASK_ENV=development yaz enterla
# sonra bu   export FLASK_APP=_1.py
# sonra flask run enter
# ctrl ^c  ile sonlandır

