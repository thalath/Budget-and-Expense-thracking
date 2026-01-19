from extensions import db
from app.models.associations import budget_categories

class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(50), unique=True, nullable=False)
    category_type = db.Column(db.String(50), nullable=False) # income/ expense
    
    budgets = db.relationship("Budget", secondary=budget_categories, back_populates="categories")
    
    
    def __repr__(self):
        return f"<Categories {self.category_type}>"
    