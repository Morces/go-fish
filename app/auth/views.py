from flask import render_template,redirect,url_for,flash,request
from . import auth
from ..models import User
from .forms import RegistrationForm,LoginForm,UpdateAccountForm
from .. import db,bcrypt
import secrets,os
from PIL import Image
from flask_login import login_user,logout_user,login_required,current_user
from ..email import mail_message



@auth.route('/register',methods=['GET','POST'])
def register():
    
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


@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join('app/static/profile_pics', picture_fn)

    output_size = (125,125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn



@auth.route('/account',methods=['GET','POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file

        current_user.username=form.username.data
        current_user.email=form.email.data
        db.session.commit()
        flash('Your account has been updated', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
  
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('profile/account.html' ,title='account', image_file=image_file, form=form)
