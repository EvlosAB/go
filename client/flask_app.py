#!/usr/bin/env python3

import requests
from database import get
from flask import Flask, redirect

app = Flask(__name__)


@app.route('/<link_name>')
def redirect_to(link_name):
    try:
        r = requests.get(f'{get.get_server_url()}/link/{link_name}')
        r.raise_for_status()

        data = r.json()
        url = data['link']['link_url']

        return redirect(url, code=301)

    except requests.HTTPError as e:
        return f'There was an error ({e})'
