# usr/bin/env python
# -*-coding:utf-8 -*-
from flask import Flask
from os import path
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import *
from flask_sqlalchemy import SQLAlchemy



basedir=path.abspath(path.dirname(__file__))
bootstrap=Bootstrap()
nav=Nav()
db=SQLAlchemy()


def create_app():
    app=Flask(__name__)
    #读取配置文件
    app.config.from_pyfile('config')
    app.config['SQLALCHEMY_DATABASE_URI'] = \
        'sqlite:///' + path.join(basedir, 'data.sqlite')
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    nav.register_element('top',Navbar(u'flask入门',
                                      View(u'主页','index'),
                                      View(u'服务','services'),
                                      View(u'关于','about'),
                                      View(u'项目','project'),
                                      View(u'登录','login')))
    db.init_app(app)
    nav.init_app(app)
    bootstrap.init_app(app)
    from auth import auth as auth_blueprint
    from main import main as main_blueprint
    #将蓝图作为实例传进去
    app.register_blueprint(auth_blueprint,url_prefix='/auth')
    #申明蓝图自己的静态文件
    app.register_blueprint(main_blueprint,static_folder='static')
    return app




