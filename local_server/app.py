from flask import Flask

application = Flask()


@application.route('/<str:link_name>')
def redirect_to(link_name):
    return 'test'
