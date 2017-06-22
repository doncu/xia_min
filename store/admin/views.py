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
    __model__ = models.Phone
    form_columns = (
        'title', 'short_title', 'price', 'description', 'category', 'rate', 'img_url_1', 'img_url_2', 'img1_1',
        'img1_2',
        'img1_3',
        'details',
    )
    column_list = (
        'title', 'short_title', 'price', 'description', 'category', 'rate', 'img_url_1', 'img_url_2', 'img1_1',
        'img1_2',
        'img1_3'
    )
    #
    form_overrides = dict(details=wtforms.TextField)
    #     title=wtforms.StringField,
    #     short_title=wtforms.StringField,
    #     price=wtforms.FloatField,
    #     description=wtforms.TextField,
    #     category=wtforms.TextField,
    #     rate=wtforms.FloatField,
    #     deta=wtforms.FloatField,
    #     img_url_1=wtforms.TextField,
    #     img_url_2=wtforms.TextField,
    #     img1_1=wtforms.TextField,
    #     img1_2=wtforms.TextField,
    #     img1_3=wtforms.TextField,
    # )

    form_extra_fields = dict(
        img_url_1=upload.ImageUploadField(base_path=config.IMG_PATH, endpoint='image'),
        img_url_2=upload.ImageUploadField(base_path=config.IMG_PATH, endpoint='image'),
        img1_1=upload.ImageUploadField(base_path=config.IMG_PATH, endpoint='image'),
        img1_2=upload.ImageUploadField(base_path=config.IMG_PATH, endpoint='image'),
        img1_3=upload.ImageUploadField(base_path=config.IMG_PATH, endpoint='image')
    )

    column_default_sort = ('id', True)
#
#
# @base.register(None, 'Detail', '/admin/detail/', 'admin.detail')
# class DetailView(base.AdminModelView):
#     __model__ = models.Detail
#     form_columns = ('phone_type', 'phone_os', 'phone_type_of_shell', 'phone_material_housing', 'phone_sim',
#                     'phone_sim_count', 'phone_weight', 'phone_screen_type', 'phone_type_of_touch_screen',
#                     'phone_diagonal', 'phone_image_size', 'phone_number_of_pixels_per_inch', 'phone_camera',
#                     'phone_camera_functions', 'phone_diaphragm', 'phone_camera_video',
#                     'phone_camera_frame_rate_of_video',
#                     'phone_geo_tagging', 'phone_front_camera', 'phone_audio', 'phone_headphone_jack', 'phone_standard_gsm',
#                     'phone_support_lte_bands', 'phone_interfaces', 'phone_satellite_navigation', 'phone_system_a_gps',
#                     'phone_support_dlna', 'phone_processor', 'phone_count_core', 'phone_video_core',
#                     'phone_built_in_memory', 'phone_ram', 'phone_battery_type', 'phone_battery_capacity',
#                     'phone_battery', 'phone_connector_type_for_charging', 'phone_sensors', 'phone_features',
#                     'phone_announcement_date', 'phone_sales_start_date',
#                     )
#
#     column_list = ('phone_type', 'phone_os', 'phone_type_of_shell', 'phone_material_housing', 'phone_sim',
#                    'phone_sim_count', 'phone_weight', 'phone_screen_type', 'phone_type_of_touch_screen',
#                    'phone_diagonal', 'phone_image_size', 'phone_number_of_pixels_per_inch', 'phone_camera',
#                    'phone_camera_functions', 'phone_diaphragm', 'phone_camera_video',
#                    'phone_camera_frame_rate_of_video',
#                    'phone_geo_tagging', 'phone_front_camera', 'phone_audio', 'phone_headphone_jack', 'phone_standard_gsm',
#                    'phone_support_lte_bands', 'phone_interfaces', 'phone_satellite_navigation', 'phone_system_a_gps',
#                    'phone_support_dlna', 'phone_processor', 'phone_count_core', 'phone_video_core',
#                    'phone_built_in_memory', 'phone_ram', 'phone_battery_type', 'phone_battery_capacity',
#                    'phone_battery', 'phone_connector_type_for_charging', 'phone_sensors', 'phone_features',
#                    'phone_announcement_date', 'phone_sales_start_date',
#                    )
#
#     form_overrides = dict(phone_type=wtforms.TextField,
#                           phone_os=wtforms.TextField,
#                           phone_type_of_shell=wtforms.TextField,
#                           phone_material_housing=wtforms.TextField,
#                           phone_sim=wtforms.TextField,
#                           phone_sim_count=wtforms.TextField,
#                           phone_weight=wtforms.TextField,
#                           phone_screen_type=wtforms.TextField,
#                           phone_type_of_touch_screen=wtforms.TextField,
#                           phone_diagonal=wtforms.TextField,
#                           phone_image_size=wtforms.TextField,
#                           phone_number_of_pixels_per_inch=wtforms.TextField,
#                           phone_camera=wtforms.TextField,
#                           phone_camera_functions=wtforms.TextField,
#                           phone_diaphragm=wtforms.TextField,
#                           phone_camera_video=wtforms.TextField,
#                           phone_camera_frame_rate_of_video=wtforms.TextField,
#                           phone_geo_tagging=wtforms.TextField,
#                           phone_front_camera=wtforms.TextField,
#                           phone_audio=wtforms.TextField,
#                           phone_headphone_jack=wtforms.TextField,
#                           phone_standard_gsm=wtforms.TextField,
#                           phone_support_lte_bands=wtforms.TextField,
#                           phone_interfaces=wtforms.TextField,
#                           phone_satellite_navigation=wtforms.TextField,
#                           phone_system_a_gps=wtforms.TextField,
#                           phone_support_dlna=wtforms.TextField,
#                           phone_processor=wtforms.TextField,
#                           phone_count_core=wtforms.TextField,
#                           phone_video_core=wtforms.TextField,
#                           phone_built_in_memory=wtforms.TextField,
#                           phone_ram=wtforms.TextField,
#                           phone_battery_type=wtforms.TextField,
#                           phone_battery_capacity=wtforms.TextField,
#                           phone_battery=wtforms.TextField,
#                           phone_connector_type_for_charging=wtforms.TextField,
#                           phone_sensors=wtforms.TextField,
#                           phone_features=wtforms.TextField,
#                           phone_announcement_date=wtforms.TextField,
#                           phone_sales_start_date=wtforms.TextField,
#                           )
