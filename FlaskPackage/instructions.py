from flask import Flask, render_template, request, Blueprint
import pypyodbc as db
import constants

instructions = Blueprint('instructions', __name__)

def getIngredients(recipeID, connection):
  cursor = connection.cursor()
  cursor.execute(constants.SELECT_RECIPEINGREDIENTS, [recipeID])
  results = cursor.fetchall()
  ingredients = []
  for row in results:
    ingredients.append(row[0] + ' ' + row[1])
  return ingredients

def getInstructions(recipeID, connection):
  cursor = connection.cursor()
  cursor.execute(constants.SELECT_RECIPEINSTRUCTIONS, [recipeID])
  results = cursor.fetchall()
  instructions = results[0][0].strip().split('\n')
  # del instructions[1:]
  return instructions

def getTitle(recipeID, connection):
  cursor = connection.cursor()
  cursor.execute(constants.SELECT_RECIPETITLE, [recipeID])
  results = cursor.fetchall()
  return results[0][0].strip()

@instructions.route('/instructions', methods = ['GET'])
def recipe():
  connection = db.connect(constants.DB_DATA.format(constants.DB_USERNAME, constants.DB_PASSWORD))

  recipe_id = request.args.get('recipeid', '0')
   
  ingredients = getIngredients(recipe_id, connection)
  instructions = getInstructions(recipe_id, connection)
  title = getTitle(recipe_id, connection)
  connection.close()

  return render_template('recipe.html',
              ingredients = ingredients,
              instructions = instructions,
              title = title)