def finance_rules(income, expense):
    tips = []

    if expense > income:
        tips.append("⚠️ Overspending detected")

    if income - expense < income * 0.2:
        tips.append("💡 Save at least 20% of income")

    if expense > income * 0.8:
        tips.append("📉 Expenses too high")

    return tips
