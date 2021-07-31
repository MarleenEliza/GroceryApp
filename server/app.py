from flask import Flask, jsonify
from flask_cors import CORS
import db

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    query = db.select_all(db.view_tables.recipe_view.value)
    return jsonify(db.read_query(db.get_connection(), query))

if __name__ == '__main__':
    app.run()
