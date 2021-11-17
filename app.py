from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>This is a home page</h1>"

@app.route('/about')
def about():
    return "<h1>This is an about page</h1>"


if __name__ == '__main__':
    app.run()
