from flask import Flask

app = Flask('blueprint_test')

app.url_map.default_subdomain = 'www' # is this done in Flask already ? It doesn't seem

from flask import Blueprint

main = Blueprint('main', 'main', subdomain='www')

@main.route('/')
def show():
    return 'Hello from main'

app.register_blueprint(main)

sub = Blueprint('sub', 'sub', subdomain='sub')

@sub.route('/')
def show2():
    return 'Hello from sub'

app.register_blueprint(sub)
