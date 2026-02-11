from extensions import db
from app.models.associations import expense_categories

# Store in Expenses table as facts 
class Expense(db.Model):
    __tablename__ = 'expenses'
    id = db.Column(db.Integer, primary_key=True, nullbale=False)
    certainty = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(255))
    
    category_id = db.relationship("Category", secondary=expense_categories, back_populates="expenses")
    
    def __repr__(self):
        return f"<Expense '{self.id}'>"