from flask import Flask

def create_app():
    app = Flask(__name__)

    # import of roads

    from app.routes.user_routes import user_bp
    app.register_blueprint(user_bp,url_prefix="/api/users")

    @app.route("/")
    def home():
        return "Bienvenue sur InFyWise"

    return app