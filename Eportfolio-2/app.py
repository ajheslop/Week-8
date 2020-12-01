from flask import Flask, render_template, redirect, request, url_for
import sqlite3
from flask_sqlalchemy import SQLAlchemy
# url for helps with the linking of dynamic pages
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test_database.db'
db = SQLAlchemy(app)


# This defines your database table
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128))

    # Define __repr__ that will be called when querying e.g. 'Users.query.all()'
    def __repr__(self):
        obj_repr = f'ID: {self.id},' \
                   f'Username: {self.username},' \
                   f'Email: {self.email},' \
                   f'Password: {self.password}' \

        return obj_repr

# python list, this needs to be defined in the route

# user the app.route decorator to define a route/endpoint


@app.route('/')
def home_index():
    posts = [
        {
            'author': {'username': 'john'},
            'body': 'Beautiful day in Gatesheeeed'
        },
        {
            'author': {'username': 'susan'},
            'body': 'the avengers movie is cool'
        },
    ]

    return render_template('index.html', title='Home')


@app.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    return render_template("signup.html")


@app.route("/confirmation", methods=["POST"])
def form():
    if request.method == "POST":

        req = request.form
        username = req.get("username")
        email = req.get("email")
        password = req.get("password")

        new_user = Users(username=username,
                     email=email,
                     password=password)

        print(new_user)
        db.session.add(new_user)
        db.session.commit()

        submission = (f"Username is:{username}\n"
                  f"Email is: {email}\n"
                  f"password is: {password}\n")

        print(submission)
    all_users = Users.query.all()

    return render_template("confirmation.html", Users=Users, all_users=all_users)

@app.route('/blog')
def blogposts():
    posts = [
        {
            'author': {'username': 'john'},
            'body': 'Beautiful day in Gatesheeeed'
        },
        {
            'author': {'username': 'susan'},
            'body': 'the avengers movie is cool'
        },
    ]
    return render_template('blog.html', title='Home', posts=posts)





if __name__ == '__main__':
    app.run(debug=True)
