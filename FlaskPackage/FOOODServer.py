import flask
import recipes
import chefs
import pypyodbc as db
import constants

APP = flask.Flask(__name__)

APP.register_blueprint(recipes.BLUEPRINT, url_prefix='/recipes')
APP.register_blueprint(chefs.BLUEPRINT, url_prefix='/chefs')

@APP.route("/")
def index():
    return flask.render_template('index.html')

def tryLogin(username, password, connection):
    cursor = connection.cursor()
    
    try:
        cursor.execute(constants.USER_LOGIN, [username, password])
        return True
    except db.Error:
        return False

@APP.route("/login.html", methods=['POST', 'GET'])
def login():
    connection = db.connect(constants.DB_DATA.format(constants.DB_USERNAME, constants.DB_PASSWORD))
    username = flask.request.form.get('username')
    password = flask.request.form.get('password')

    success = False
    if username and password:
        success = tryLogin(username, password, connection)
    
    connection.close()
    return flask.render_template('login.html', success=success)

if __name__ == "__main__":
    APP.run(debug=True)
