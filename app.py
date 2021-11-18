
from flask import Flask, render_template, url_for, request
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
    return render_template('index.html')

@app.route('/about')
def about():
    list_names = ["Noureddine", "Ayoub", "Meryam", "Siham"]
    return render_template('about.html', names=list_names)

@app.route('/bootstrap')
def bootstrap():
    return render_template('bootstrap.html')

@app.route('/subscribe')
def subscribe():
    return render_template('subscribe.html')

@app.route('/form_att', methods=["POST"])
def form_att():
    email = request.form.get("email")
    password = request.form.get("password")
    return render_template('form_att.html', email=email, password=password)


if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.run()

