import flask
import pypyodbc as db
import constants

BLUEPRINT = flask.Blueprint('instructions', __name__)

def get_ingredients(recipe_id, connection):
    cursor = connection.cursor()
    cursor.execute(constants.SELECT_RECIPEINGREDIENTS, [recipe_id])
    results = cursor.fetchall()
    ingredients = []
    for row in results:
        ingredients.append(row[0] + ' ' + row[1])
    return ingredients

def get_instructions(recipe_id, connection):
    cursor = connection.cursor()
    cursor.execute(constants.SELECT_RECIPEINSTRUCTIONS, [recipe_id])
    results = cursor.fetchall()
    instructions = results[0][0].strip().split('\n')
    return instructions

def get_title(recipe_id, connection):
    cursor = connection.cursor()
    cursor.execute(constants.SELECT_RECIPETITLE, [recipe_id])
    results = cursor.fetchall()
    return results[0][0].strip()

@BLUEPRINT.route('/', methods=['GET'])
def recipe():
    connection = db.connect(constants.DB_DATA.format(constants.DB_USERNAME, constants.DB_PASSWORD))

    recipe_id = flask.request.args.get('recipeid', '0')
    ingredients = get_ingredients(recipe_id, connection)
    instructions = get_instructions(recipe_id, connection)
    title = get_title(recipe_id, connection)
    connection.close()

    return flask.render_template('recipe.html',
                                 ingredients=ingredients,
                                 instructions=instructions,
                                 title=title)
