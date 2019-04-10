from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Token(db.Model):
    __tablename__ = 'tokens'

    token_id = db.Column(db.Integer(), primary_key=True)
    token_name = db.Column(db.String(80), nullable=False)
    token = db.Column(db.String(120), nullable=False)

    def generate_random_token(self):
        return 1234

    def __init__(self, token_name):
        self.token_name = token_name
        self.token = self.generate_random_token()

    def get_dict(self):
        return {
            'token_id': self.token_id,
            'token_name': self.token_name,
        }


class Link(db.Model):
    __tablename__ = 'links'

    link_id = db.Column(db.Integer(), primary_key=True)
    link_name = db.Column(db.String(80), nullable=False)
    link_url = db.Column(db.TEXT, nullable=False)

    def get_dict(self):
        return {
            'link_id': self.link_id,
            'link_name': self.link_name,
            'link_url': self.link_url,
        }
