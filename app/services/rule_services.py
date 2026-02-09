from extensions import db
from typing import List, Optional
from app.models.expense_budget import Rule

class RuleService:
    
    @staticmethod
    def get_all() -> List[Rule]:
        return Rule.query.order_by(Rule.id.asc()).all()

    @staticmethod
    def get_by_id(rule_id: str) -> Optional[Rule]:
        return Rule.query.get(rule_id)
    
    @staticmethod
    def create(data: dict) -> Rule:
        rule = Rule(
            id = data["id"],
            conditions = data["conditions"],
            conclusion = data["conclusion"],
            certainty = data["certainty"],
            explanation = data["explanation"],
        )
        
        try:
            db.session.add(rule)
            db.session.commit()
        except Exception:
            db.session.rollback()
            raise
        finally:
            db.session.close()

        return rule
    
    @staticmethod
    def update(rule: Rule, data: dict) -> Rule:
        rule.id = data["id"]
        rule.conditions = data["conditions"]
        rule.conclusion = data["conclusion"]
        rule.certainty = data.get("ceratainty", 0.0)
        rule.explanation = data.get("explanation", "_")
        
        db.session.commit()
        return rule
    
    @staticmethod
    def delete(rule_id: str) -> None:
        db.session.delete(rule_id)
        db.session.commit()
    