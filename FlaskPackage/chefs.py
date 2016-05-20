import flask
import pypyodbc as db
import constants

BLUEPRINT = flask.Blueprint('chefs', __name__)

def getChefList(email, speciality, connection):
	cursor = connection.cursor()
	if (speciality and email):	
		cursor.execute(constants.SELECT_CHEFS_BY_EMAIL_S, [email, speciality])
	elif speciality:
		cursor.execute(constants.SELECT_CHEFS_BY_SPECIALITY, [speciality])
	elif email:
		cursor.execute(constants.SELECT_CHEFS_BY_EMAIL, [email])
	else:
		return []
	results = cursor.fetchall()
	chefs = []
	for row in results:
		chefs.append({'id':str(row[0]), 'email':row[2], 'speciality':row[1]})

	return chefs


@BLUEPRINT.route('/search.html', methods=['GET'])
def show_instructions():
    connection = db.connect(constants.DB_DATA.format(constants.DB_USERNAME, constants.DB_PASSWORD))
    chefemail = flask.request.args.get('email')
    speciality = flask.request.args.get('speciality')

    chefs = getChefList(chefemail, speciality, connection)

    connection.close()
    return flask.render_template('chefs/search.html', title='Search Results', chefs=chefs)
