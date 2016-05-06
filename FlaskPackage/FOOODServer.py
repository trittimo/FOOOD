from flask import Flask, render_template, request
import sys, getopt
import pypyodbc as db
    

app = Flask(__name__)

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
    cursor = connection.cursor()

    recipe_id = request.args.get('recipeid', '0')
   
    SQLCommand = "SELECT Taste FROM Ingredient WHERE Name = '" + ingredient + "'"
    cursor.execute(SQLCommand)
    results = cursor.fetchall()
    connection.close()

    ingredients = ["1 x Egg", "1 x Ham", "1 Liter Green Food Coloring"]
    instructions = ["Cook the egg", "Roast the ham", "Apply green food coloring", "Serve"]
    title = "Green Eggs and Ham"

    return render_template('recipe.html',
                            ingredients = ingredients,
                            instructions = instructions,
                            title = title)

if __name__ == "__main__":
    app.run(debug = True)