"""Jose Reyes
SDEV300
Lab 8"""

from datetime import datetime
from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, login_required, LoginManager
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'HOGS'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_in_user(user_id):
    """ load in user"""
    return Users.query.get(int(user_id))


# initialize the database
db = SQLAlchemy(app)


# create model
class Users(db.Model, UserMixin):
    """Users class"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)


class Login_Form(FlaskForm):
    """Login form"""
    username = StringField(validators=[InputRequired()], render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[InputRequired(), Length(min=12, max=25)],
                             render_kw={"placeholder": "Password"})
    submit = SubmitField("Log in")


class Reg_Form(FlaskForm):
    """sign up form"""
    username = StringField(validators=[InputRequired(), Length(min=2, max=80)],
                           render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[InputRequired(), Length(min=12, max=25)]
                             , render_kw={"placeholder": "Password"})
    name = StringField(validators=[InputRequired(), Length(min=2, max=80)],
                       render_kw={"placeholder": "Name"})
    submit = SubmitField("Sign UP")


class Reset_Form(FlaskForm):
    """Reset form"""
    username = StringField(validators=[InputRequired()], render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[InputRequired(), Length(min=12, max=25)],
                             render_kw={"placeholder": "New Password"})
    name = StringField(validators=[InputRequired(), Length(min=2, max=80)],
                       render_kw={"placeholder": "Current Name or New Name"})

    submit = SubmitField("Reset")


@app.route('/forgot', methods=["POST", "GET"])
@login_required
def forgot():
    form = Reset_Form()
    if form.validate_on_submit():
        user = Users.query.filter_by(username=form.username.data).first()
        if user:
            db.session.delete(user)
            secure_password = bcrypt.generate_password_hash(form.password.data)
            new_user = Users(name=form.name.data, username=form.username.data, password=secure_password)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('check_login'))

    """Update password"""
    return render_template('forgot.html', form=form)


@app.route('/home')
@login_required
def index():
    """Home Page"""
    return render_template("index.html")


@app.route('/', methods=["POST", "GET"])
def check_login():
    """Login page"""
    form = Login_Form()

    if form.validate_on_submit():
        user = Users.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('index'))
        else:
            flash("Login Unsuccessful")
            return redirect(url_for('check_login'))

    return render_template('login.html', form=form)


@app.route('/signup', methods=["GET", "POST"])
def signup():
    """sign up page"""
    form = Reg_Form()

    if form.validate_on_submit():
        secure_password = bcrypt.generate_password_hash(form.password.data)
        new_user = Users(name=form.name.data, username=form.username.data, password=secure_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('check_login'))

    return render_template("signup.html", form=form)


@app.route('/page2')
@login_required
def depth():
    """Page 2 """
    return render_template("page2.html")


@app.route('/page3')
@login_required
def schedule():
    """Page 3"""
    return render_template("page3.html")


@app.route('/time')
@login_required
def time():
    """Time Page"""
    date = datetime.now()
    return "Today's date is " + str(date)


if __name__ == "__main__":
    app.run(debug=True)
