import flask
import pypyodbc as db
import constants

BLUEPRINT = flask.Blueprint('users', __name__)

def try_login(username, password, connection):
    cursor = connection.cursor()
    try:
        cursor.execute(constants.USER_LOGIN_1, [username, password])
        cursor.execute(constants.USER_LOGIN_2, [username])
        results = cursor.fetchone()
        if results:
            return results[0]
        else:
            return -1
    except db.Error as e:
        print(e)
        return -1

def delete_order(order, username, connection):
    print("Deleting " + str(order) + " from " + str(username))
    cursor = connection.cursor()
    cursor.execute(constants.DELETE_ORDER, [order])
    
    return get_orders(username, cursor)

def get_orders(username, cursor):
    cursor.execute(constants.SELECT_ORDERS, [username])
    results = cursor.fetchall()
    orders = []
    for row in results:
        orders.append({'id':row[0], 'chef':row[1], 'price':round(row[2],2), 'time':row[3]})
    return orders

@BLUEPRINT.route('/view-orders.html', methods=['POST', 'GET'])
def vieworders():
    connection = db.connect(constants.DB_DATA.format(constants.DB_USERNAME, constants.DB_PASSWORD))
    username = flask.request.form.get('username')
    password = flask.request.form.get('password')

    order = flask.request.form.get('id')
    session = flask.request.form.get('session')
    user = flask.request.form.get('user')

    if order and session:
        orders = delete_order(order, user, connection)
        connection.close()
        return flask.render_template('user/view-orders.html', orders=orders, sessionID=session, username=user)

    sessionID = False
    if username and password:
        sessionID = try_login(username, password, connection)
    else:
        connection.close()
        return flask.render_template('user/view-orders.html')

    if sessionID == -1:
        connection.close()
        return flask.render_template('user/view-orders.html', badlogin=True)
    else:
        orders = get_orders(username, connection.cursor())
        connection.close()
        return flask.render_template('user/view-orders.html', orders=orders, sessionID=sessionID, username=username)

def add_order(username, email, recipe, connection):
    cursor = connection.cursor()
    cursor.execute(constants.INSERT_ORDER, [username, email, recipe])
    cursor.fetchall()
    return

@BLUEPRINT.route('/order.html', methods=['POST', 'GET'])
def order():
    # TODO
    return flask.render_template('user/order.html')

@BLUEPRINT.route('/login.html', methods=['POST', 'GET'])
def login():
    connection = db.connect(constants.DB_DATA.format(constants.DB_USERNAME, constants.DB_PASSWORD))
    username = flask.request.form.get('username')
    password = flask.request.form.get('password')

    sessionID = False
    if username and password:
        sessionID = try_login(username, password, connection)
    
    connection.close()
    return flask.render_template('user/login.html', sessionID=sessionID)