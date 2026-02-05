# app/models/associations.py
from extensions import db

user_roles = db.Table(
    "user_roles",
    db.Column("user_id", db.Integer, db.ForeignKey("users.id"), primary_key=True),
    db.Column("role_id", db.Integer, db.ForeignKey("roles.id"), primary_key=True),
)

role_permissions = db.Table(
    "role_permissions",
    db.Column("role_id", db.Integer, db.ForeignKey("roles.id"), primary_key=True),
    db.Column("permission_id", db.Integer, db.ForeignKey("permissions.id"), primary_key=True),
)

category_budget = db.Table(
    "category_budgets",
    db.Column("category_id", db.Integer, db.ForeignKey("categories.id"), primary_key=True),
    db.Column("budget_id", db.Integer, db.ForeignKey("budgets.id"), primary_key=True)
)

category_expenses = db.Table(
    "category_expenses",
    db.Column("category_id", db.Integer, db.ForeignKey("categories.id"), primary_key=True),
    db.Column("expense_id", db.Integer, db.ForeignKey("expenses.id"), primary_key=True)
)