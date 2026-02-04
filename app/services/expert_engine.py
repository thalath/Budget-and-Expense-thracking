from app.models.expense_budget import Budget, Expense
from extensions import db
from sqlalchemy import func

def analyze_category(category_id):
    budget = Budget.query.filter_by(category_id=category_id).first()

    total = db.session.query(
        func.sum(Expense.amount)
    ).filter_by(category_id=category_id).scalar() or 0

    if not budget:
        return "No budget defined"

    if total > budget.amount:
        return "❌ Budget exceeded"
    elif total >= 0.8 * budget.amount:
        return "⚠️ Close to budget limit"
    else:
        return "✅ Spending is under control"
