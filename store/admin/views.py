from flask import flash
from flask import url_for
from flask import request
from flask import redirect
from flask import render_template

from flask_login import login_user
from flask_login import logout_user
from flask_login import LoginManager

from flask_admin.form import upload

import wtforms

import config

from store.app import app
from store import models
from store.admin import base
from store.admin import models as admin_models

login_manager = LoginManager(app)
login_manager.user_loader(admin_models.get_user)
login_manager.login_view = 'users.login'
login_manager.login_message = 'Login success'
login_manager.login_message_category = 'info'


@app.route('/admin/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        verify, user = admin_models.check_user(username, password)
        if verify:
            login_user(user)
            return redirect('/admin/')
        else:
            flash('Введен неправильный логин или пароль', 'error')

    return render_template('admin/login.html')


@app.route('/admin/logout/')
def logout():
    logout_user()
    return redirect(url_for('login'))


@base.register(None, 'User', '/admin/users/', 'admin.user')
class UserView(base.AdminModelView):
    __model__ = admin_models.User
    column_list = ('username', 'is_admin')
    form_columns = ('username', 'password', 'is_admin')

    form_overrides = dict(username=wtforms.StringField, is_admin=wtforms.BooleanField, password=wtforms.PasswordField)
    column_default_sort = ('username', None)


@base.register(None, 'Phones', '/admin/phones/', 'admin.phones')
class PhonesView(base.AdminModelView):
    __model__ = models.Phones
    form_columns = ('title', 'short_title', 'price', 'description', 'category', 'rate', 'img_url_1', 'img_url_2', 'img1_1', 'img1_2', 'img1_3')
    column_list = ('title', 'short_title', 'price', 'description', 'category', 'rate', 'img_url_1', 'img_url_2', 'img1_1', 'img1_2', 'img1_3')

    form_overrides = dict(
        title=wtforms.StringField,
        short_title=wtforms.StringField,
        price=wtforms.FloatField,
        description=wtforms.TextField,
        category=wtforms.TextField,
        rate=wtforms.FloatField,
        img_url_1=wtforms.TextField,
        img_url_2=wtforms.TextField,
        img1_1=wtforms.TextField,
        img1_2=wtforms.TextField,
        img1_3=wtforms.TextField,
    )

    form_extra_fields = dict(img_url_1=upload.ImageUploadField(base_path=config.IMG_PATH, endpoint='image'),
                             img_url_2=upload.ImageUploadField(base_path=config.IMG_PATH, endpoint='image'),
                             img1_1=upload.ImageUploadField(base_path=config.IMG_PATH, endpoint='image'),
                             img1_2=upload.ImageUploadField(base_path=config.IMG_PATH, endpoint='image'),
                             img1_3=upload.ImageUploadField(base_path=config.IMG_PATH, endpoint='image'),
                             )

    column_default_sort = ('id', True)
