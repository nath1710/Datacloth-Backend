from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config
from flask_cors import CORS

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    CORS(app)
    
    app.config.from_object(Config)

    db.init_app(app)

    from .routes import main
    app.register_blueprint(main)

    return app
