from typing import List, Optional
from app.models.expense_budget import Budget, Category
from extensions import db

class BudgetService:
    @staticmethod
    def get_all_budget() -> List[Budget]:
        return Budget.query.order_by(Budget.id.desc()).all()
    
    @staticmethod
    def get_Budget_by_id(Budget_id: int) -> Optional[Budget]:
        return Budget.query.get(Budget_id)
    
    @staticmethod
    def create_Budget(data: dict, category_id: Optional[int] = None) -> Budget:
        budget = Budget(
            amount = data["amount"]
        )
        if category_id:
            c = db.session.get(Category, category_id)
            if c:
                budget.category_id = [c]
        db.session.add(budget)
        db.session.commit()
        return budget
    
    @staticmethod
    def update_Budget(budget: Budget, data: dict, category_id: Optional[int] = None) -> Budget:
        budget.amount = data["amount"]
        if category_id:
            c = db.session.get(Category, category_id)
            if c:
                budget.category_id = [c]
                
        db.session.commit()
        return budget
    
    @staticmethod
    def delete(budget: Budget) -> None:
        db.session.delete(budget)
        db.session.commit()