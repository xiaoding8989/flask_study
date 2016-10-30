# usr/bin/env python
# -*-coding:utf-8 -*-
from os import path
from flask_sqlalchemy import SQLAlchemy
from  . import db

#数据库的配置
#db=SQLAlchemy(app)
#设计数据库模型
class Role(db.Model):
    __tablename__='roles'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String,nullable=True)
    user=db.relationship('User',backref='role')

    @staticmethod
    def seed():
        db.session.add_all(map(lambda  r:Role(name=r),['Gest','Administrators']))
        db.session.commit()

class User(db.Model):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String,nullable=True)
    password=db.Column(db.String,nullable=True)
    role_id=db.Column(db.Integer,db.ForeignKey('roles.id'))

    @staticmethod
    def on_created(target,value,initiator):
        target.role=Role.query.filter_by(name='Guests').first()
db.event.listen(User.name,'set',User.on_created)

@login_manger.user_loader
def get_user(user_id):
    return User.query.filter_by(name=user_id).first()














