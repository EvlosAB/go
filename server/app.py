#!/usr/bin/env python3
from json import dumps, loads
from flask import Flask, request, make_response
from .models import db, Token, Link

app = Flask(__name__)
db.init_app(app)


def return_data(data, status_code=200, json=True):
    json_data = dumps(data)
    response = make_response(json_data)

    if json:
        response.headers['Content-Type'] = 'application/json'
    response.status_code = status_code

    return response


@app.route("/hello", methods=['GET'])
def hello():
    return return_data(
            {'message': 'Hello there! Everything works as expected.'})


@app.route('/link', methods=['GET', 'POST'])
def link():
    if request.method == 'POST':
        json_data = request.get_json()
        data = loads(json_data)

        link_name = data['link_name']
        link_url = data['link_url']

        # Add link to database
        link = Link(link_name=link_name, link_url=link_url)

        db.session.add(token)
        db.session.commit()

    elif request.method == 'GET':
        link_name = request.args.get('link', None)
        link = Link.query.filter_by(link_name=link_name).first()

        if not link:
            return return_data({}, 404)

        return return_data({'link': link.get_dict()})


@app.route("/links", methods=['GET'])
def links():
    return return_data(
        {
            'links': [link.get_dict() for link in Link.query.all()],
        }
    )


@app.route('/token', methods=['POST'])
def token():
    json_data = request.get_json()
    data = loads(json_data)
    token_name = data['token_name']

    # Add token to database
    token = Token(token_name)
    db.session.add(token)
    db.session.commit()

    return return_data({
        'token': token.get_dict(),
        'token_token': token.token
    }, 201)


@app.route('/tokens', methods=['GET'])
def tokens():
    return return_data({
        'tokens': [token.get_dict() for token in Token.query.all()]
    })


if __name__ == '__main__':
    app.run(debug=True)
