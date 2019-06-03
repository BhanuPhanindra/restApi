from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/test")
def hello1():
    return "Inner path test"

app.route("/test/tt")
def hello2():
    return "Inner path test again"


if __name__ == '__main__':
    app.run(debug=True)