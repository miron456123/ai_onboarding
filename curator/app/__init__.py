from flask import Flask
from .config import Config
from .db import db, migrate


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    from .blueprints.employee import bp as employee_bp
    from .blueprints.admin import bp as admin_bp
    from .blueprints.api import bp as api_bp
    app.register_blueprint(employee_bp)
    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(api_bp, url_prefix='/api')

    return app
