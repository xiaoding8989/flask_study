# usr/bin/env python
# -*-coding:utf-8 -*-
from flask import Flask,render_template,request,redirect,url_for,flash
from werkzeug.routing import BaseConverter
from os import path
from werkzeug.utils import secure_filename



class RegexConverter(BaseConverter):
    def __init__(self,url_map,*item):
        super(RegexConverter,self).__init__(url_map)
        self.regex=item[0]
#给转换器起个名字
def init_views(app):
    app.url_map.converters['regex']=RegexConverter
    @app.route('/')
    def index():
        return render_template('index.html',title="<h1>Welcome</>",
                               body="##Header2")


    @app.route('/about')
    def about():
        return "I am about"

    @app.route('/services')
    def services():
        return "I am services"

    @app.route('/project')
    def project():
        return "I am project"

    @app.route('/user/<username>/')
    def user(username):
        return "User %s"%username

    @app.route('/user/<regex("[a-z]{3}"):user_id>/')
    def userr(user_id):
        return "User %d"%user_id

    @app.route('/upload',methods=['GET','POST'])
    def upload():
        if request.method=="POST":
            f=request.files['files']
            basepath=path.abspath(path.dirname(__file__))
            upload_path=path.join(basepath,'static/uploads')
            f.save(upload_path+'/'+secure_filename(f.filename))
            return redirect(url_for('upload'))
        return render_template('upload.html')

    def read_md(filename):
        with open(filename,'r') as md_file:
            content=reduce(lambda x,y:x+y,md_file.readlines())
        return content.decode('utf-8')

    @app.template_test('current_link')
    def is_current_link(link):
        return link==request.path

    @app.context_processor
    def inject_methods():
        return dict(read_md=read_md)
