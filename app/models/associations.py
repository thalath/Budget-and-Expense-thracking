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


user_transactions = db.Table(
    "user_transactions",
    db.Column("user_id", db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column("transactions_id", db.Integer, db.ForeignKey('transactions.id'), primary_key=True)
)

user_budgets = db.Table(
    "user_budgets",
    db.Column("user_id", db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column("budget_id", db.Integer, db.ForeignKey('budgets.id'), primary_key=True)
)

budget_categories = db.Table(
    "budget_categories",
    db.Column("budget_id", db.Integer, db.ForeignKey('budgets.id'), primary_key=True),
    db.Column("category_id", db.Integer, db.ForeignKey("categories.id"), primary_key=True)
)

user_recommendations = db.Table(
    "user_recommendations",
    db.Column("user_id", db.Integer, db.ForeignKey("users.id"), primary_key=True),
    db.Column("recommendation_id", db.Integer, db.ForeignKey("recommendations.id"), primary_key=True)
)

user_expertRules = db.Table(
    "user_expertRules",
    db.Column("user_id", db.Integer, db.ForeignKey("users.id"), primary_key=True),
    db.Column("expertRule_id", db.Integer, db.ForeignKey("expert_rules.id"), primary_key=True)
    
)

expert_recommendation = db.Table(
    "ex_recommendation",
    db.Column("expert_rule_id", db.Integer, db.ForeignKey("expert_rules.id"), primary_key=True),
    db.Column("recommendation_id", db.Integer, db.ForeignKey("recommendations.id"), primary_key=True)
)