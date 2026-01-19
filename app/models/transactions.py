from extensions import db
from datetime import datetime
from app.models.associations import user_transactions

class Transactions(db.Model):
    __tablename__ = 'transactions'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    transaction_type = db.Column(db.String(15), nullable=False)
    description = db.Column(db.String(255))
    
    users = db.relationship("User", secondary=user_transactions, back_populates="transactions")
    
    def __repr__(self):
        return f"<Transactions {self.amount} >"
    
    