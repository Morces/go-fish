from . import db,login_manager
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#Model Class for User
class User(db.Model,UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    email=db.Column(db.String(255),unique=True,nullable=False)
    username = db.Column(db.String(250),nullable=False)
    pass_secure = db.Column(db.String(255),nullable=True)
    image_file=db.Column(db.String(30),nullable=False,default='default.jpg')
    bio = db.Column(db.String(300))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)


    def __repr__(self):
        return f'User {self.username}'