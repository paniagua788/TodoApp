import os

from flask import Flask

def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY='HONEY',
        DATABASE_HOST=os.environ.get('FLASK_DATABASE_HOST'),
        DATABASE_PASSWORD=os.environ.get('FLASK_DATABASE_PASSWORD'),
        DATABASE_USER=os.environ.get('FLASK_DATABASE_USER'),
        DATABASE=os.environ.get('FLASK_DATABASE')
    )

    app.route('/index')
    def index():
        return 'ToDo List'
    
    return app