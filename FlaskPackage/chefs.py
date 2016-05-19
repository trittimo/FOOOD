import flask
import pypyodbc as db
import constants

BLUEPRINT = flask.Blueprint('chefs', __name__)

def getChefList(email, id, speciality, connection):
	cursor = connection.cursor()
	if speciality:	
		if not email:
			cursor.execute(constants.SELECT_CHEFS_BY_ID_S, [id, speciality])
		else:
			cursor.execute(constants.SELECT_CHEFS_BY_EMAIL_S, [email, speciality])
	else:
		if not email:
			cursor.execute(constants.SELECT_CHEFS_BY_ID, [id])
		else:
			cursor.execute(constants.SELECT_CHEFS_BY_EMAIL, [email])
	results = cursor.fetchall()
	chefs = []
	for row in results:
		# TODO table form
		chefs.append({'id':str(row[0]), 'email':row[2], 'speciality':row[1]})
		# chefs.append('<td>ID</td><td>' + str(row[0]) + '</td><td>Speciality</td><td>' + row[1] + '</td><td>Email</td><td>' + row[2] + '</td>')

	return chefs


@BLUEPRINT.route('/search.html', methods=['GET'])
def show_instructions():
    connection = db.connect(constants.DB_DATA.format(constants.DB_USERNAME, constants.DB_PASSWORD))
    chefemail = flask.request.args.get('email')
    chefid = flask.request.args.get('id')
    speciality = flask.request.args.get('speciality')

    if not (chefemail or chefid):
    	return flask.render_template('chefs/search.html', title='Search for a Chef')

    chefs = getChefList(chefemail, chefid, speciality, connection)

    connection.close()
    return flask.render_template('chefs/search.html', title='Search Results', chefs=chefs)
