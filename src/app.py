from flask import Flask, render_template
from flask_cors import CORS, cross_origin

from config import config

# Routes
from routes import cuentas

app = Flask(__name__)

CORS(app, resources={r"/api/*": {"origins": "*"}})


def page_not_found(error):
    return "<h1>Not found page</h1>", 404

@app.after_request
def after_request(response):
    response.headers.remove('Access-Control-Allow-Origin')
    response.headers.remove('Access-Control-Allow-Methods')
    response.headers.remove('Access-Control-Allow-Headers')
    return response


if __name__ == '__main__':
    app.config.from_object(config['development'])

    # Blueprints
    app.register_blueprint(cuentas.main, url_prefix='/api/cuentas')

    # Error handlers
    app.register_error_handler(404, page_not_found)
    app.run()