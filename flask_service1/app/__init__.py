import subprocess
from flask import Flask
from custom_package.db_handler import register_models


def create_app():
    app = Flask(__name__)
    register_models()
    subprocess.run(["alembic", "upgrade", "head"], check=True)
    with app.app_context():
        from app.customers.urls import customers_routes
        app.register_blueprint(customers_routes)
        return app
