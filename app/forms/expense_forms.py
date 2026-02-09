from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, FloatField
from wtforms.validators import DataRequired, Length
from app.models.expense_budget import Category, Expense
from extensions import db

def _category_choices():
    return [
        (c.id, c.name)
        for c in db.session.scalars(
            db.select(Category).order_by(Category.name)
        )
    ]
    
    
class ExpenseCreateForm(FlaskForm):
    
    id = StringField(
        "ID",
        validators=[DataRequired(), Length(min=2, max=10, message="The value must be less than 10 characters")],
        render_kw={"placeholder": "Enter fact id e.g. f1"}
    )
    
    amount = FloatField(
        "Enter Amount",
        validators=[DataRequired()],
        render_kw={"placeholder": "Enter amount"}
    )
    
    category_id = SelectField(
        "Select Category",
        coerce=int,
        validators=[DataRequired()],
        render_kw={"placeholder": "Select Category"}
    )
    
    submit = SubmitField("Save")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.category_id.choices = _category_choices()
        
class ExpenseEditForm(FlaskForm):
    id = StringField(
        "ID",
        validators=[DataRequired(), Length(min=2, max=10, message="The value must be less than 10 characters")],
        render_kw={"placeholder": "Enter fact id e.g. f1"}
    )
    
    amount = FloatField(
        "Enter Amount",
        validators=[DataRequired()],
        render_kw={"placeholder": "Enter amount"}
    )
    
    category_id = SelectField(
        "Select Category",
        coerce=int,
        validators=[DataRequired()],
        render_kw={"placeholder": "Select Category"}
    )
    
    submit = SubmitField("Update")

    def __init__(self, original_expense: Expense, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.original_expense = original_expense
        self.category_id.choices = _category_choices()
        
        if not self.is_submitted():
            if original_expense.categories:
                self.category_id.data = original_expense.categories[0].id
            else:
                self.category_id.data = None
                
class ExpenseConfirmDeleteForm(FlaskForm):
    submit = SubmitField("Confirm Delete")