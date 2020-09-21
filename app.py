from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

@app.route('/<lastname>')
def hello_lastname(lastname):
    return "Hello {}!".format(lastname)

if __name__ == '__main__':
    app.run()