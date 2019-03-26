from flask import Flask, jsonify
from flask_cors import CORS

DEBUG = True

# instantiating our app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app)

# checking our routing
@app.route('/main', methods=['GET'])
def ping_pong():
    return jsonify('home_screen')


if __name__ == '__main__':
    app.run()

