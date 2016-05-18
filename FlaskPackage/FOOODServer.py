import flask
import pypyodbc as db
import constants
from instructions import instructions


app = flask.Flask(__name__)

app.register_blueprint(instructions)

@app.route("/")
def index():
  return "Do something"

if __name__ == "__main__":
  app.run(debug = True)
  # app.run()