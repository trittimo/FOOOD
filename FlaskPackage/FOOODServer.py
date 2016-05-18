"""The server for FOOOD"""

import flask
import instructions


APP = flask.Flask(__name__)

APP.register_blueprint(instructions.blueprint, url_prefix='/instructions')

@APP.route("/")
def index():
    """Returns the index page when we browse the root of the site"""
    return flask.render_template('index.html')

if __name__ == "__main__":
    APP.run(debug=True)
