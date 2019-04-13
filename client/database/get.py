from database import models
from database import db


def get_server_url():
    return db.session.query(models.Setting) \
            .filter_by(setting_name='url').first().setting_value


def get_token_name():
    return db.session.query(models.Setting) \
            .filter_by(setting_name='token_name').first().setting_value


def get_token():
    return db.session.query(models.Setting) \
            .filter_by(setting_name='token').first().setting_value
