from flask import Flask, render_template, request
import sys, getopt
import pypyodbc as db
    

app = Flask(__name__)

def getIngredients(recipeID, connection):
    cursor = connection.cursor()
    cursor.execute('SELECT Amount, IngredientName '
                    'FROM Uses '
                    'WHERE RecipeID=' + recipeID)
    results = cursor.fetchall()
    ingredients = []
    for row in results:
        ingredients.append(row[0] + ' ' + row[1])
    return ingredients

def getInstructions(recipeID, connection):
    cursor = connection.cursor()
    cursor.execute('SELECT Instructions '
                   'FROM Recipe '
                   'WHERE RecipeID=' + recipeID)
    results = cursor.fetchall()
    instructions = results[0][0].strip().split('\n')
    # del instructions[1:]
    return instructions

def getTitle(recipeID, connection):
    cursor = connection.cursor()
    cursor.execute('SELECT RecipeName '
                   'FROM Recipe '
                   'WHERE RecipeID=' + recipeID)
    results = cursor.fetchall()
    return results[0][0].strip()

@app.route('/recipe.html', methods = ['GET'])
def recipe():
    try:
        optlist, args = getopt.getopt(sys.argv[1:], '', ['username', 'password'])
    except getopt.GetoptError as err:
        print(err)
        sys.exit(2)

    username = args[0]
    password = args[2]

    connection = db.connect('Driver={SQL Server};'
                            'Server=titan.csse.rose-hulman.edu;'
                            'Database=The_FOOOD;'
                            'uid=' + username +
                            ';pwd=' + password)

    recipe_id = request.args.get('recipeid', '0')
   
    ingredients = getIngredients(recipe_id, connection)
    instructions = getInstructions(recipe_id, connection)
    title = getTitle(recipe_id, connection)
    connection.close()

    # ingredients = ["1 x Egg", "1 x Ham", "1 Liter Green Food Coloring"]
    # instructions = ["Cook the egg", "Roast the ham", "Apply green food coloring", "Serve"]
    # title = "Green Eggs and Ham"

    return render_template('recipe.html',
                            ingredients = ingredients,
                            instructions = instructions,
                            title = title)

if __name__ == "__main__":
    app.run(debug = True)