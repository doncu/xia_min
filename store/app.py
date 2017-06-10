from flask import Flask
from flask_admin import Admin

import config
from store import db
from store.admin import index
from store import common

app = Flask(__name__)
app.config.from_object('config')
admin = Admin(
    app,
    name='admin',
    index_view=index.AdminIndexView(url='/admin/'),
    base_template='admin/master.html',
    template_mode='bootstrap3'
)


app.add_template_global(common.chunks, 'chunks')


@app.teardown_request
def remove_session(*args):
    db.session.rollback()
    db.session.remove()


from store import views
from store.admin import views
