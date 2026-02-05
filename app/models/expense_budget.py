from extensions import db
from datetime import datetime
from app.models.associations import category_budget as cb, category_expenses as ce

class Category(db.Model):
    __tablename__ = "categories"
    id = db.Column(db.Integer, primary_key=True)
    # budget_id = db.Column(db.Integer, db.ForeignKey("budgets.id"))
    name = db.Column(db.String(100), unique=True, nullable=False)

    budgets = db.relationship("Budget", secondary=cb, back_populates="categories")
    expenses = db.relationship("Expense", secondary=ce, back_populates="categories")


class Budget(db.Model):
    __tablename__ = "budgets"
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"))
    amount = db.Column(db.Float, nullable=False)
    
    categories = db.relationship("Category", secondary=cb, back_populates="budgets")
    
class Expense(db.Model):
    __tablename__="expenses"
    id = db.Column(db.Integer, primary_key=True)
    # category_id = db.Column(db.Integer, db.ForeignKey("categories.id"))
    amount = db.Column(db.Float, nullable=False)
    expense_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    expense_updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    
    categories = db.relationship("Category", secondary=ce, back_populates="expenses")
    
class Rule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    condition = db.Column(db.String(255), nullable=False)
    conclusion = db.Column(db.String(255), nullable=False)