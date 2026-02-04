from extensions import db
from datetime import date

class Category(db.Model):
    __tablename__ = "categories"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

    budgets = db.relationship("Budget", backref="category_ref", lazy=True)
    expenses = db.relationship("Expense", backref="category_ref", lazy=True)


class Budget(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"))
    amount = db.Column(db.Float, nullable=False)
    
class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"))
    amount = db.Column(db.Float, nullable=False)
    expense_date = db.Column(db.Date, default=date.today)
    
class Rule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    condition = db.Column(db.String(255), nullable=False)
    conclusion = db.Column(db.String(255), nullable=False)