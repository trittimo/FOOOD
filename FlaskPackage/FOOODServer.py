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

    ingredient = request.args.get('ingredient', 'Beef')
   
    SQLCommand = "SELECT Taste FROM Ingredient WHERE Name = '" + ingredient + "'"
    cursor.execute(SQLCommand)
    results = cursor.fetchall()
    connection.close()
    
    return results[0]
    # return render_template('recipe.html')

if __name__ == "__main__":
    app.run(debug = True)