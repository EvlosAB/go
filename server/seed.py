#!/usr/bin/env python3
from flask import Flask
from .models import *

if __name__ == '__main__':
    app = Flask(__name__)
    db.init_app(app)
    db.create_all()
    db.session.commit()
