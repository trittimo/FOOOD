"""The server for FOOOD"""

import flask
import recipes


APP = flask.Flask(__name__)

APP.register_blueprint(recipes.BLUEPRINT, url_prefix='/recipes')

@APP.route("/")
def index():
    return flask.render_template('index.html')

if __name__ == "__main__":
    APP.run(debug=True)
