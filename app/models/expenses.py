from extensions import db
from datetime import datetime
from app.models.associations import expense_categories, expense_budgets


# Store in Expenses table as facts 
class Expense(db.Model):
    __tablename__ = 'expenses'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    certainty = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    
    categories = db.relationship("Category", secondary=expense_categories, back_populates="expenses")
    budgets = db.relationship("Budget", secondary=expense_budgets, back_populates="expenses")
    
    def __repr__(self):
        return f"<Expense '{self.id}'>"