
from flask import Flask, render_template, url_for, request, redirect
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
bootstrap = Bootstrap(app)

# SQLAlchemy with flask :
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///finals.db'

# Initialize the database
db = SQLAlchemy(app)

# Create db model :
class finals(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    # Create a function to return a string when wwe add a friend :
    def __repr__(self):
        return f"< name : {self.id}>"


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

@app.route('/form_att', methods=["POST","GET"])
def form_att():
    email = request.form.get("email")
    password = request.form.get("password")
    return render_template('form_att.html', email=email, password=password)

@app.route('/final', methods=["POST","GET"])
def final():
    if request.method == "POST":
        subscriber_name = request.form["name"]
        new_subscriber = finals(name=subscriber_name)

    #     Push It Into The DataBase :
        try:
            db.session.add(new_subscriber)
            db.session.commit()
            return redirect("/final")
        except:
            return "There was a problem when we try to add it the database"


    else:
        friends = finals.query.order_by(finals.date_created)
        return render_template('final.html', friends=friends)

if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.run()

