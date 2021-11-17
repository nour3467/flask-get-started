
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['TESTING'] = True
app.config['TEMPLATES_AUTO_RELOAD'] = True

title = "Noureddine ft. flask"

@app.route('/')
def index():
    return render_template('index.html', title=title)

@app.route('/about')
def about():
    list_names = ["Noureddine", "Ayoub", "Meryam", "Siham"]
    return render_template('about.html', title=title, names=list_names)

@app.route('/bootstrap')
def bootstrap():
    return render_template('bootstrap.html',title=title)


if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.run()

