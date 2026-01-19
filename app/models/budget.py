from extensions import db
from datetime import datetime
from app.models.associations import budget_categories, user_budgets


class Budget(db.Model):
    __tablename__ = 'budgets'
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    period = db.Column(db.String(50), nullable=False)
    start_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    
    users = db.relationship("User", secondary=user_budgets, back_populates="budgets")
    categories = db.relationship("Category", secondary=budget_categories, back_populates="budgets")
    
    
    def __repr__(self):
        return f"<Budgets {self.period}>"

    