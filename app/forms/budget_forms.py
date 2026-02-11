from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
from app.forms.multi_checkbox_field import MultiCheckBoxField
from app.models.expenses import Expense
from app.models.budgets import Budget
from extensions import db

def _expense_choices():
    return [
        (e.id, e.category_id)
        for e in db.session.scalars(
            db.select(Expense).order_by(Expense.category_id)
        )
    ]

class BudgetCreateForm(FlaskForm):
    
    income = FloatField(
        "Income",
        validators=[DataRequired()],
        render_kw={"placeholder": "enter Your monthly income"}
    )
    
    expense_id = MultiCheckBoxField(
        "Expense",
        coerce=int,
        render_kw={"placeholder": "total expense, monthly..!"}
    )
    
    description = TextAreaField(
        "Description",
        validators=[DataRequired()],
        render_kw={"placeholder": "description"}
    )
    
    submit = SubmitField("Save")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.expense_id.choices = _expense_choices()
        
class BudgetEditForm(FlaskForm):
    
    income = FloatField(
        "Income",
        validators=[DataRequired()],
        render_kw={"placeholder": "enter Your monthly income"}
    )
    
    expense_id = MultiCheckBoxField(
        "Expense",
        coerce=int,
        render_kw={"placeholder": "total expense, monthly..!"}
    )
    
    description = TextAreaField(
        "Description",
        validators=[DataRequired()],
        render_kw={"placeholder": "description"}
    )
    
    submit = SubmitField("Update")

    def __init__(self,original_budget: Budget, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.original_budget = original_budget
        self.expense_id.choices = _expense_choices()
        
class BudgetConfirmDeleteForm(FlaskForm):
    submit = SubmitField("Confirm Delete")