import sqlalchemy as sa

from store import db


class Phones(db.Base):
    __tablename__ = 'phones'
    id = sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.String(80), index=True, nullable=False)
    short_title = sa.Column(sa.String(20), index=True, nullable=False)
    price = sa.Column(sa.Float(asdecimal=True, index=True, decimal_return_scale=True), nullable=False)
    description = sa.Column(sa.Text, nullable=False, index=True)
    category = sa.Column(sa.Text, nullable=False, index=True)
    img_url_1 = sa.Column(sa.Text, nullable=False, index=True)
    img_url_2 = sa.Column(sa.Text, nullable=False, index=True)
    img1_1 = sa.Column(sa.Text, nullable=False, index=True)
    img1_2 = sa.Column(sa.Text, nullable=False, index=True)
    img1_3 = sa.Column(sa.Text, nullable=False, index=True)
    rate = sa.Column(sa.Float(asdecimal=True, index=True, decimal_return_scale=True), nullable=False)
