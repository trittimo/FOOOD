import flask
import pypyodbc as db
import constants

BLUEPRINT = flask.Blueprint('users', __name__)

def try_login(username, password, connection):
    cursor = connection.cursor()
    try:
        cursor.execute(constants.USER_LOGIN, [username, password])
        return True
    except db.Error:
        return False

@BLUEPRINT.route('/vieworders.html', methods=['POST', 'GET'])
def vieworders():
    # TODO
    return flask.render_template('user/order.html')

@BLUEPRINT.route('/order.html', methods=['POST', 'GET'])
def order():
    # TODO
    return flask.render_template('user/order.html')

@BLUEPRINT.route('/login.html', methods=['POST', 'GET'])
def login():
    connection = db.connect(constants.DB_DATA.format(constants.DB_USERNAME, constants.DB_PASSWORD))
    username = flask.request.form.get('username')
    password = flask.request.form.get('password')

    success = False
    if username and password:
        success = try_login(username, password, connection)
    
    connection.close()
    return flask.render_template('user/login.html', success=success)