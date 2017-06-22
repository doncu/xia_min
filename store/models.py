import sqlalchemy as sa

from store import db
from store import common


class Phone(db.Base):
    __tablename__ = 'phones'
    id = sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.String(80), index=True, nullable=False)
    short_title = sa.Column(sa.String(20), index=True, nullable=False)
    price = sa.Column(sa.Float(asdecimal=True, index=True, decimal_return_scale=True), nullable=False)
    rate = sa.Column(sa.Float(asdecimal=True, index=True, decimal_return_scale=True), nullable=False)

    category = sa.Column(sa.Text, nullable=False)
    description = sa.Column(sa.Text, nullable=False)
    img_url_1 = sa.Column(sa.Text, nullable=False)
    img_url_2 = sa.Column(sa.Text, nullable=False)
    img1_1 = sa.Column(sa.Text, nullable=False)
    img1_2 = sa.Column(sa.Text, nullable=False)
    img1_3 = sa.Column(sa.Text, nullable=False)


class Attr(db.Base):
    __tablename__ = 'attrs'

    TYPES = ['Integer', 'Float', 'Any', 'Text']

    id = sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.Text, nullable=False)
    type = sa.Column(sa.Text, nullable=False)


class PhoneAttr(db.Base):
    __tablename__ = 'phone_attr'

    phone_id = sa.Column(sa.ForeignKey('phones.id'))
    attr_id = sa.Column(sa.ForeignKey('attrs.id'))
    value = sa.Column(sa.Text)


def check_value(attr, value):
    type_map = {
        'Text': lambda value, **kwargs: True,
        'Any': lambda value, values, **kwargs: value in values,

    }


# class Image(db.Base):
#     id = sa.Column(sa.Integer, primary_key=True)
#     path = sa.Column(sa.Text)
#
#
# class GalleryImage(db.Base):
#     image_id = sa.Column()
#     phone_id = sa.Column()
#     order = sa.Column(sa.Integer)
#     main = sa.Column(sa.Boolean)


# class Detail(db.Base):
#     __tablename__ = 'detail'
#     id = sa.Column(sa.Integer, primary_key=True)
#     phone_id = sa.Column(sa.Integer, sa.ForeignKey('phones.id'))
#     phone_type = sa.Column(sa.Text, nullable=False, index=True)
#     phone_os = sa.Column(sa.Text, nullable=False, index=True)
#     phone_type_of_shell = sa.Column(sa.Text, nullable=False, index=True)
#     phone_material_housing = sa.Column(sa.Text, nullable=False, index=True)
#     phone_sim = sa.Column(sa.Text, nullable=False, index=True)
#     phone_sim_count = sa.Column(sa.Text, nullable=False, index=True)
#     phone_weight = sa.Column(sa.Text, nullable=False, index=True)
#     phone_screen_type = sa.Column(sa.Text, nullable=False, index=True)
#     phone_type_of_touch_screen = sa.Column(sa.Text, nullable=False, index=True)
#     phone_diagonal = sa.Column(sa.Text, nullable=False, index=True)
#     phone_image_size = sa.Column(sa.Text, nullable=False, index=True)
#     phone_number_of_pixels_per_inch = sa.Column(sa.Text, nullable=False, index=True)
#     phone_camera = sa.Column(sa.Text, nullable=False, index=True)
#     phone_camera_functions = sa.Column(sa.Text, nullable=False, index=True)
#     phone_diaphragm = sa.Column(sa.Text, nullable=False, index=True)
#     phone_camera_video = sa.Column(sa.Text, nullable=False, index=True)
#     phone_camera_frame_rate_of_video = sa.Column(sa.Text, nullable=False, index=True)
#     phone_geo_tagging = sa.Column(sa.Text, nullable=False, index=True)
#     phone_front_camera = sa.Column(sa.Text, nullable=False, index=True)
#     phone_audio = sa.Column(sa.Text, nullable=False, index=True)
#     phone_headphone_jack = sa.Column(sa.Text, nullable=False, index=True)
#     phone_standard_gsm = sa.Column(sa.Text, nullable=False, index=True)
#     phone_support_lte_bands = sa.Column(sa.Text, nullable=False, index=True)
#     phone_interfaces = sa.Column(sa.Text, nullable=False, index=True)
#     phone_satellite_navigation = sa.Column(sa.Text, nullable=False, index=True)
#     phone_system_a_gps = sa.Column(sa.Text, nullable=False, index=True)
#     phone_support_dlna = sa.Column(sa.Text, nullable=False, index=True)
#     phone_processor = sa.Column(sa.Text, nullable=False, index=True)
#     phone_count_core = sa.Column(sa.Integer, nullable=False, index=True)
#     phone_video_core = sa.Column(sa.Text, nullable=False, index=True)
#     phone_built_in_memory = sa.Column(sa.Text, nullable=False, index=True)
#     phone_ram = sa.Column(sa.Text, nullable=False, index=True)
#     phone_battery_type = sa.Column(sa.Text, nullable=False, index=True)
#     phone_battery_capacity = sa.Column(sa.Text, nullable=False, index=True)
#     phone_battery = sa.Column(sa.Text, nullable=False, index=True)
#     phone_connector_type_for_charging = sa.Column(sa.Text, nullable=False, index=True)
#     phone_sensors = sa.Column(sa.Text, nullable=False, index=True)
#     phone_features = sa.Column(sa.Text, nullable=False, index=True)
#     phone_announcement_date = sa.Column(sa.Text, nullable=False, index=True)
#     phone_sales_start_date = sa.Column(sa.Text, nullable=False, index=True)

