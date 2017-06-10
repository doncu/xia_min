import os

BASE_PATH = os.path.abspath(os.path.dirname(__file__))
#TEMPLATE_PATH = os.path.abspath(os.path.join(BASE_PATH, 'templates'))
#STATIC_PATH = os.path.abspath(os.path.join(BASE_PATH, 'static'))
IMG_PATH = os.environ.get('IMG_PATH', os.path.join(BASE_PATH, 'images'))

DATABASE_URI = 'sqlite:///{}'.format(os.environ.get('DATABASE_URI', os.path.join(BASE_PATH, 'store.db')))
# DATABASE_URI = 'mysql://store:storepass@localhost/shop'

CSRF_ENABLED = True
SECRET_KEY = 'tYpzfysZZJqIb4X5OVYE4nve1UPKnz0IRRaYzDC40n'
