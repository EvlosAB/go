import os
import requests
from json import dumps, loads
from flask import Flask, request, make_response, redirect
from .models import db, Token, Link

app = Flask(__name__)
db.init_app(app)

DATABASE_NAME = os.environ['MYSQL_DATABASE']
DATABASE_USER = os.environ['MYSQL_USER']
DATABASE_PASSWORD = os.environ['MYSQL_PASSWORD']
DATABASE_HOST = os.environ['MYSQL_HOST']
DATABASE_PORT = os.environ['MYSQL_PORT']

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{DATABASE_USER}:'
f'{DATABASE_PASSWORD}@{DATABASE_HOST}:'
f'{DATABASE_PORT}/{DATABASE_NAME}'


def delete_database():
    with app.app_context():
        db.drop_all()
        db.session.commit()


def create_database():
    with app.app_context():
        db.create_all()
        db.session.commit()


def return_data(data, status_code=200, json=True):
    json_data = dumps(data)
    response = make_response(json_data)

    if json:
        response.headers['Content-Type'] = 'application/json'
    response.status_code = status_code

    return response


@app.route('/<link_name>')
def redirect_to(link_name):
    try:
        r = requests.get(f'{request.url_root}link/{link_name}')
        r.raise_for_status()

        data = r.json()
        url = data['link']['link_url']

        return redirect(url, code=301)

    except requests.HTTPError as e:
        return f'There was an error ({e})'


@app.route("/hello", methods=['GET'])
def hello():
    return return_data(
            {'message': 'Hello there! Everything works as expected.'})


@app.route('/link/<link_name>', methods=['GET', 'DELETE'])
def specific_link(link_name):
    link = Link.query.filter_by(link_name=link_name).first()
    if not link:
        return return_data({}, 404)

    # GET method
    if request.method == 'GET':
        return return_data({'link': link.get_dict()})

    # DELETE method
    db.session.delete(link)
    db.session.commit()

    # Return 204 No Content as the entry was deleted
    return return_data({}, 204)


@app.route('/link', methods=['POST'])
def link():
    data = request.get_json()
    link_name = data['link_name']
    link_url = data['link_url']

    previous_link = Link.query.filter_by(link_name=link_name).first()
    if previous_link:
        return return_data(
            {'message': 'A link with that name already exists'}, 409)

    # Add link to database
    link = Link(link_name=link_name, link_url=link_url)

    db.session.add(link)
    db.session.commit()

    return return_data({'link': link.get_dict()}, 201)


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
