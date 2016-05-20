import flask
import pypyodbc as db
import constants

BLUEPRINT = flask.Blueprint('recipes', __name__)

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

@BLUEPRINT.route('/recipe.html', methods=['GET'])
def show_instructions():
    connection = db.connect(constants.DB_DATA.format(constants.DB_USERNAME, constants.DB_PASSWORD))

    recipe_id = flask.request.args.get('recipeid')
    if not recipe_id:
        connection.close()
        return flask.render_template('recipes/recipe.html', title="Unknown Recipe")

    ingredients = get_ingredients(recipe_id, connection)
    instructions = get_instructions(recipe_id, connection)
    title = get_title(recipe_id, connection)
    connection.close()

    return flask.render_template('recipes/recipe.html',
                                 ingredients=ingredients,
                                 instructions=instructions,
                                 title=title)

@BLUEPRINT.route('/search-by-ingredients.html', methods=['GET','POST'])
def search_by_ingredients():
    return flask.render_template('recipes/search-by-ingredients.html')

def find_recipes_with_name(name, connection):
    if not name:
        return []
    cursor = connection.cursor()
    cursor.execute(constants.SELECT_RECIPES_BY_NAME, [name])
    results = cursor.fetchall()
    recipes = []
    for row in results:
        recipes.append({'name':row[1],'price':round(row[3],2),'id':row[0]})

    return recipes


@BLUEPRINT.route('/search-by-name.html', methods=['GET'])
def search_by_name():
    connection = db.connect(constants.DB_DATA.format(constants.DB_USERNAME, constants.DB_PASSWORD))
    
    recipe = flask.request.args.get('recipe')
    result = find_recipes_with_name(recipe, connection)
    
    connection.close()
    return flask.render_template('recipes/search-by-name.html', recipes=result)