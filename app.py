from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Development
from flask_migrate import Migrate



app = Flask(__name__)
app.config.from_object(Development)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from mod_users import users

@app.route('/')
def hello_world():
    return 'Hello World!'


from mod_admin import admin

app.register_blueprint(admin)
app.register_blueprint(users)

if __name__ == '__main__':
    app.run()
