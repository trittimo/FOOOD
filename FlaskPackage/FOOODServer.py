import flask
import recipes
import chefs
import users
import pypyodbc as db
import constants

APP = flask.Flask(__name__)

APP.register_blueprint(recipes.BLUEPRINT, url_prefix='/recipes')
APP.register_blueprint(chefs.BLUEPRINT, url_prefix='/chefs')
APP.register_blueprint(users.BLUEPRINT, url_prefix='/user')

@APP.route('/')
def index():
    return flask.render_template('index.html')

if __name__ == "__main__":
    APP.run(debug=True, host='0.0.0.0')
