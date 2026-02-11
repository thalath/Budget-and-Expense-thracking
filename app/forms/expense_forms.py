from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired
from app.models.categories import Category
from app.models.expenses import Expense
from extensions import db

def _category_choices():
    return [
        (c.id, c.name)
        for c in db.session.scalars(
            db.select(Category).order_by(Category.name)
        )
    ]
    
class ExpenseCreateForm(FlaskForm):
    category_id = SelectField(
        "Category",
        validators=[DataRequired()],
        coerce=int,
        render_kw={"placeholder": "Select Category"}
    )
    
    certainty = FloatField(
        "Certainty",
        validators=[DataRequired()],
        default=0.00,
    )
    
    description = TextAreaField(
        "Description",
        render_kw={"placeholder": "Description"}
    )
    
    submit = SubmitField("Save")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.category_id.choices = _category_choices()
    
class ExpenseEditForm(FlaskForm):
    category_id = SelectField(
        "Category",
        validators=[DataRequired()],
        coerce=int,
        render_kw={"placeholder": "Select Category"}
    )
    
    certainty = FloatField(
        "Certainty",
        validators=[DataRequired()],
        default=0.00,
    )
    
    description = TextAreaField(
        "Description",
        render_kw={"placeholder": "Description"}
    )
    
    submit = SubmitField("Update")

    def __init__(self,original_expense: Expense, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.original_expense = original_expense
        self.category_id.choices = _category_choices()
        
class ExpenseConfirmDelete(FlaskForm):
    submit = SubmitField("Confirm Delete")