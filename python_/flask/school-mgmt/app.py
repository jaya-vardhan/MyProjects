from api_flask import ApiFlask
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost/practice1"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_ECHO'] = False


db = SQLAlchemy(app)
# db.init_app(app)
migrate = Migrate(app, db)
# migrate.init_app(app, db)
from models import *


@app.route('/', methods=['GET'])
def index():
    print("index")
        
    return {
        "message": f"Flask is working and ip is {request.remote_addr}"
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
