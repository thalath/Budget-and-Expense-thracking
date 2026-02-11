from typing import List, Optional
from app.models.categories import Category
from extensions import db


class CategoryService:
    
    @staticmethod
    def get_all() -> List[Category]:
        return Category.query.order_by(Category.name.asc()).all()

    @staticmethod
    def get_by_id(category_id: int) -> Optional[Category]:
        return Category.query.get(category_id)
    
    def create(data: dict) -> Category:
        category = Category(
            name = data['name'],
            description = data['description'] or '_'
        )
        
        db.session.add(category)
        db.session.commit()
        return category
    
    @staticmethod
    def update(category: Category, data: dict) -> Category:
        category.name = data["name"]
        category.description = data.get("descriptions", "")

        db.session.commit()
        return category
    
    @staticmethod
    def delete(category: Category) -> None:
        db.session.delete(category)
        db.session.commit()
