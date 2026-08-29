# from flask import Flask
# from flask_cors import CORS

# from config import Config
# from app.extensions import db


# def create_app():
#     app = Flask(__name__)

#     app.config.from_object(Config)

#     CORS(app)

#     db.init_app(app)

#     return app

from flask import Flask
from config import Config
from app.extensions import db, migrate, cors

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app)

    # register blueprints here as you build them
    # from app.blueprints.auth import auth_bp
    # app.register_blueprint(auth_bp)

    @app.route('/')
    def health_check():
        return {'status': 'BotaniQ backend is running'}

    return app