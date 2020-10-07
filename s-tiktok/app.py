from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
  return 'Server Works!'
  
@app.route('/<toto>')
def say_hello(toto):
    user = request.args.get('user')
    return 'Hello ' + toto + user +  ' !!!'