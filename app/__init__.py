from flask import Flask, redirect, url_for, render_template
from config import Config
from extensions import db, csrf, login_manager
from app.models.user import User

def create_app(config_class: type[Config] = Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Init extensions
    db.init_app(app)
    csrf.init_app(app)
    login_manager.init_app(app)

    # Flask-Login settings
    login_manager.login_view = "auth.login"
    login_manager.login_message = "Please log in to access this page"
    login_manager.login_message_category = "warning"

    @login_manager.user_loader
    def load_user(user_id: str):
        return User.query.get(int(user_id))
    
    # register blueprint
    from app.routes.user_routes import user_bp
    from app.routes.role_routes import role_bp
    from app.routes.permission_routes import permission_bp
    from app.routes.auth_routes import auth_bp
    from app.routes.transaction_routes import transaction_bp
    
    app.register_blueprint(user_bp)
    app.register_blueprint(role_bp)
    app.register_blueprint(permission_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(transaction_bp)

    # 👇 Add this block to "/" goes to the users list
    @app.route("/")
    def home():
        return redirect(url_for('transaction.list_transactions'))

    # Create tables
    with app.app_context():
        from app.models.user import User # noqa F401
        from app.models.role import Role
        from app.models.permission import Permission
        from app.models.transaction import Transaction
        db.create_all()

    return app