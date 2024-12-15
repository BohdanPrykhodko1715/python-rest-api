from flask import Flask, jsonify
from flask_smorest import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from config import Config


db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    api = Api(app)
    jwt = JWTManager(app)

    from app.views import bp
    api.register_blueprint(bp)

    @app.errorhandler(400)
    def bad_request_error(e):
        return jsonify({"message": "Bad Request", "details": str(e)}), 400
    
    @app.errorhandler(401)
    def unauthorized_error(e):
        return jsonify({"message": "Unauthorized", "details": str(e)}), 401
    
    @app.errorhandler(404)
    def not_found_error(e):
        return jsonify({"message": "Resource not found"}), 404
    
    @app.errorhandler(500)
    def internal_server_error(e):
        return jsonify({"message": "Internal Server Error"}), 500
    
    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return jsonify({"message": "The token has expired", "error": "token_expired"}), 401
    
    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return jsonify({"message": "Invalid token", "error": "invalid_token"}), 401
    
    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return jsonify({"message": "Missing token", "error": "authorization_required"}), 401

    return app

