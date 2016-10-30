# usr/bin/env python
# -*-coding:utf-8 -*-
from flask import Flask,render_template,request,redirect,url_for,flash
from werkzeug.routing import BaseConverter
from os import path
from werkzeug.utils import secure_filename
from . import main

@main.route('/about')
def about():
    return "I am about"

@main.route('/services')
def services():
    return "I am services"

@main.route('/project')
def project():
    return "I am project"

@main.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'),404

@main.template_test('current_link')
def is_current_link(link):
    return link == request.path
