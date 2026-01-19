from extensions import db
from app.models.associations import expert_recommendation, user_expertRules

class ExpertRule(db.Model):
    __tablename__ = "expert_rules"
    id = db.Column(db.Integer, primary_key=True)
    condition = db.Column(db.String(100), nullable=False)
    serverity = db.Column(db.String(100), nullable=False) # High, Medium, Low
    certainty = db.Column(db.Float, nullable=False)
    explanation = db.Column(db.String(255))
    
    
    users = db.relationship("User", secondary=user_expertRules, back_populates="expert_rules")
    recommendations = db.relationship("Recommendation", secondary=expert_recommendation, back_populates="expert_rules")
    
    
    def __repr__(self) -> str:
        return f"<ExpertRule {self.condition}>"
        