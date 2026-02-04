from typing import List, Optional
from app.models.expense_budget import Category
from extensions import db

class CategoryService:
    @staticmethod
    def get_all_category() -> List[Category]:
        return Category.query.order_by(Category.id.desc()).all()
    
    @staticmethod
    def get_category_by_id(category_id: int) -> Optional[Category]:
        return Category.query.get(category_id)
    
    @staticmethod
    def create_category(data: dict) -> Category:
        category = Category(
            name=data["name"]
        )
        db.session.add(category)
        db.session.commit()
        return category
    
    @staticmethod
    def update_category(category: Category, data: dict) -> Category:
        category.name = data["name"]
        db.session.commit()
        return category
    
    @staticmethod
    def delete(category: Category) -> None:
        db.session.delete(category)
        db.session.commit()