from typing import List, Optional
from app.models.expense_budget import Expense, Category
from extensions import db

class ExpenseService:
    
    @staticmethod
    def get_all_expense() -> List[Expense]:
        return Expense.query.order_by(Expense.id.asc()).all()

    @staticmethod
    def get_by_id(expense_id: int) -> Optional[Expense]:
        return Expense.query.get(expense_id)
    
    @staticmethod
    def create(data: dict, category_id: Optional[int] = None) -> Expense:
        expense = Expense(
            amount = data["amount"],
        )
        if category_id:
            c = db.session.get(Category, category_id)
            if c:
                expense.category_id = [c]

        db.session.add(expense)
        db.session.commit()
        return expense
    
    @staticmethod
    def update(expense: Expense, data: dict, category_id: Optional[int] = None) -> Expense:
        expense.amount = data["amount"] or 0
        if category_id:
            c = db.session.get(Category, category_id)
            if c:
                expense.categories = [c]
        
        db.session.add(expense)
        db.session.commit()
        return expense
    
    @staticmethod
    def delete(expense: Expense) -> None:
        db.session.delete(expense)
        db.session.commit()
        
            
        