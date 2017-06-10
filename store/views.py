import os
import imghdr

from flask import views
from flask import session
from flask import url_for
from flask import request
from flask import redirect
from flask import send_file
from flask import render_template

from store import db
from store import models
from store.app import app

import config


@app.route('/', endpoint='index')
def index_view():
    return render_template('index.html')


@app.route('/about_us')
def about_us_view():
    return render_template('about_us.html')


@app.route('/test')
def test():
    #data = dict(phones=db.session.query(models.Phones).order_by(models.Phones.id).all())
    return render_template('production.html')


@app.route('/products/')
def category_view():
    phones = db.session.query(models.Phones).order_by(models.Phones.id).all()
    return render_template('products.html', phones=phones)


@app.route('/product/<int:oid>')
def product_view(oid):
    phone = db.session.query(models.Phones).get(oid)
    return render_template('product.html', item=phone)


@app.route('/contacts')
def contacts_view():
    return render_template('contacts.html')


@app.route('/basket')
def shopcart_view():
    return render_template('basket.html')


@app.route('/img/<filename>', endpoint='image')
def image_view(filename):
    full_path = os.path.join(config.IMG_PATH, filename)
    type_ = imghdr.what(full_path)
    return send_file(full_path, mimetype='image/{}'.format(type_))
