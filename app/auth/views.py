from flask import render_template,redirect,url_for
from . import auth
from ..models import User
from .forms import RegistrationForm
from .. import db,bcrypt
import secrets,os
from PIL import Image
from flask_login import login_user,logout_user,login_required,current_user



@auth.route('/login')
def login():
    return render_template('auth/login.html')


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