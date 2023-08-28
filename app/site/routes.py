from flask import Blueprint, render_template
from forms import UserSignUpForm, LoginForm

site = Blueprint('site', __name__, template_folder='site_templates')

@site.route('/')
def home():
    return render_template('index.html')

@site.route('/register')
def register():
    form = UserSignUpForm()
    return render_template('sign_up.html', title='Register', form=form)

@site.route('/LogIn')
def LogIn():
    form = LoginForm()
    return render_template('sign_in.html', title='Sign-In', form=form)

@site.route('/cars')
def cars():
    return render_template('cars.html')