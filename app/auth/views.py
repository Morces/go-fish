from flask import render_template,redirect,url_for,flash,request
from . import auth
from ..models import User
from .forms import RegistrationForm,LoginForm
from .. import db,bcrypt
import secrets,os
from PIL import Image
from flask_login import login_user,logout_user,login_required,current_user
from ..email import mail_message



@auth.route('/register',methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('.index'))
    form =RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, pass_secure=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in' , 'success')
        
        mail_message("Welcome to go-fish","email/welcome_user",user.email,user=user)
        return redirect(url_for('auth.login'))
    
    return render_template('auth/register.html' ,title='register' ,form=form) 


@auth.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form =LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.pass_secure, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page= request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.index'))
        else:    
            flash("Login unsuccesful.Please check email and password",'danger')

    return render_template('auth/login.html' ,title='login', form=form)  