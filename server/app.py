from flask import Flask, jsonify
from flask_cors import CORS
from db import main as db
from db.tables import view_tables

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# sanity check route


@app.route('/viewTable', methods=['GET'])
def getViewTable():
    query = db.select_all(view_tables.recipe_view.value)
    return jsonify(db.read_query(db.get_connection(), query))


if __name__ == '__main__':
    app.run()
