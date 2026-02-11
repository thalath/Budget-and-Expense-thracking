from app.routes.user_routes import user_bp
from app.routes.role_routes import role_bp
from app.routes.permission_routes import permission_bp
from app.routes.auth_routes import auth_bp
from app.routes.category_routes import category_bp
from app.routes.expense_routes import expense_bp

__all__ = [
    "user_bp",
    "role_bp",
    "permission_bp",
    "auth_bp",
    "category_bp",
    "expense_bp"
]