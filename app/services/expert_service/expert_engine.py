from services.expert_service.rules import finance_rules

def analyze(transactions):
    income = sum(t.amount for t in transactions if t.type == "income")
    expense = sum(t.amount for t in transactions if t.type == "expense")

    return {
        "income": income,
        "expense": expense,
        "balance": income - expense,
        "tips": finance_rules(income, expense)
    }
