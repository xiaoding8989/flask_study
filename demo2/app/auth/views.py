# usr/bin/env python
# -*-coding:utf-8 -*-
from flask import Flask,render_template,request,redirect,url_for,flash
from . import auth

@auth.route('/login',method=['GET','POST'])
def login():
    return render_template('login.html',title=u'登录',form=form)

@auth.route('/register',method=['GET','POST'])
def login():
    return render_template('register.html',title=u'注册')