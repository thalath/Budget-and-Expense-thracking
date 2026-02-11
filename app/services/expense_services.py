from extensions import db
from app.models.expenses import Expense
from typing import List, Optional
from app.models.categories import Category

class ExpenseService:
    
    @staticmethod
    def get_all() -> List[Expense]:
        return Expense.query.order_by(Expense.category_id.asc()).all()

    @staticmethod
    def get_by_id(expense_id: int) -> Optional[Expense]:
        return Expense.query.get(expense_id)

    @staticmethod
    def create(data: dict, category_id: Optional[int] = None) -> Optional[Expense]:
        expense = Expense(
            certainty = data["certainty"],
            description = data["description"],
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
        expense.category_id =data.get("category_id")
        expense.certainty = data.get("certainty")
        
        if category_id:
            c = db.session.get(Category, category_id)
            if c:
                expense.category_id = [c]
                
        db.session.commit()
        return expense

    @staticmethod
    def delete(expense: Expense) -> None:
        db.session.delete(expense)
        db.session.commit()
    
    