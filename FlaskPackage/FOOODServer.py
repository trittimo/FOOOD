import flask
import pypyodbc as db
import constants
import instructions


app = flask.Flask(__name__)

app.register_blueprint(instructions.blueprint, url_prefix = '/instructions')

@app.route("/")
def index():
  return flask.render_template('index.html')

if __name__ == "__main__":
  app.run(debug = True) # TODO: debug = False