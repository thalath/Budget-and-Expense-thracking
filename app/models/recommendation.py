from extensions import db
from datetime import datetime
from app.models.associations import expert_recommendation, user_expertRules

class Recommendation(db.Model):
    __tablename__ = 'recommendations'
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(255))
    date_generated = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    
    
    # users = db.relationship("User", secondary=user_expertRules, back_populates="recommendations")
    expert_rules = db.relationship("ExpertRule", secondary=expert_recommendation, back_populates="recommendations")
    def __repr__(self):
        return f"<Recommendations {self.message}>"