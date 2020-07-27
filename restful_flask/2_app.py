from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/database.db'

db = SQLAlchemy(app)

if __name__ == "__main__":
    app.run(debug=True)
