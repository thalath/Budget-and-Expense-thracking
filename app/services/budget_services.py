from extensions import db
from app.models.budgets import Budget
from typing import List, Optional
from app.models.expenses import Expense

class BudgetService:
    
    @staticmethod
    def get_all() -> List[Budget]:
        return Budget.query.order_by(Budget.income.asc()).all()

    @staticmethod
    def get_by_id(budget_id: int) -> Optional[Budget]:
        return Budget.query.get(budget_id)
    
    @staticmethod
    def create(data: dict, expense_id: Optional[int] = None) -> Budget:
        budget =Budget(
            income = data["income"],
            needed = data["needed"],
            wanted = data["wanted"],
            savings = data["savings"],
            having_fun = data["having_fun"],
            descripion = data["description"]
        )
        
        if expense_id:
            e = db.session.get(Expense, expense_id)
            if e:
                budget.expense_id = [e]
                
        db.session.add(budget)
        db.session.commit()
        return budget

    @staticmethod
    def update(budget: Budget, data: dict, expense_id: Optional[int] = None) -> Budget:
        budget.income = data["income"]
        budget.needed = data["needed"]
        budget.wanted = data["wanted"]
        budget.savings = data["savings"]
        budget.having_fun = data["having_fun"]
        budget.description = data["description"]

        if expense_id:
            e = db.session.get(Expense, expense_id)
            if e:
                budget.expenses = [e]

        db.session.commit()
        return budget

    @staticmethod
    def delete(budget: Budget) -> None:
        db.session.delete(budget)
        db.session.commit()