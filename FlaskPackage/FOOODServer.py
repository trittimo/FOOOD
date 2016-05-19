"""The server for FOOOD"""

import flask
import recipes
import chefs


APP = flask.Flask(__name__)

APP.register_blueprint(recipes.BLUEPRINT, url_prefix='/recipes')
APP.register_blueprint(chefs.BLUEPRINT, url_prefix='/chefs')

@APP.route("/")
def index():
    return flask.render_template('index.html')

if __name__ == "__main__":
    APP.run(debug=True)
