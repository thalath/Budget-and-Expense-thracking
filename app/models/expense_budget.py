from extensions import db
from datetime import date
from app.models.associations import category_budget as cb

class Category(db.Model):
    __tablename__ = "categories"
    id = db.Column(db.Integer, primary_key=True)
    budget_id = db.Column(db.Integer, db.ForeignKey("budgets.id"))
    name = db.Column(db.String(100), unique=True, nullable=False)

    budgets = db.relationship("Budget", secondary=cb, back_populates="categories")
    expenses = db.relationship("Expense", backref="category_ref", lazy=True)


class Budget(db.Model):
    __tablename__ = "budgets"
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"))
    amount = db.Column(db.Float, nullable=False)
    
    categories = db.relationship("Category", secondary=cb, back_populates="budgets")
    
class Expense(db.Model):
    __tablename__="expenses"
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"))
    amount = db.Column(db.Float, nullable=False)
    expense_date = db.Column(db.Date, default=date.today)
    
class Rule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    condition = db.Column(db.String(255), nullable=False)
    conclusion = db.Column(db.String(255), nullable=False)