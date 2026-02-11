from extensions import db
from app.models.associations import expense_budgets

# Create the budgets table to stored as rule 
class Budget(db.Model):
    __tablename__='budgets'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    income = db.Column(db.Float, nullable=False)
    needed = db.Column(db.Float, nullable=False)
    wanted = db.Column(db.Float, nullable=False)
    savings = db.Column(db.Float, nullable=False)
    having_fun = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(255))
    
    expense_id = db.relationship("Expenses", secondary=expense_budgets, back_populates="budgets")
    
    def __repr__(self):
        return f"<Budget '{self.name}'>"