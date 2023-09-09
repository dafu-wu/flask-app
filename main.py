# simple_app.py

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to our Flask app!"

@app.route('/greet/<name>')
def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
