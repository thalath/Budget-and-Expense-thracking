from extensions import db
from datetime import datetime
from app.models.associations import expense_categories

class Category(db.Model):
    __tablename__="categories"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), unique=True, nullable=False)
    description = db.Column(db.String(255))
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    
    expenses = db.relationship("Expense", secondary=expense_categories, back_populates="categories")
    
    def __repr__(self) -> set[str]:
        return f"<Category '{self.name}'>"