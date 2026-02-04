from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, FloatField
from wtforms.validators import DataRequired
from extensions import db
from app.models.expense_budget import Budget, Category

def _category_choice():
    """Return List of Category from Category id"""
    return [
        (c.id, c.name)
        for c in db.session.scalars(
            db.select(Category).order_by(Category.name)
        )
    ]
    
class BudgetCreateForm(FlaskForm):
    category_id = SelectField(
        "Category",
        coerce=int,
        validators=[DataRequired()],
        render_kw={"placeholder": "Enter Category"}
    )
    
    amount = FloatField(
        "Enter amout($)",
        validators=[DataRequired()],
        render_kw={"placeholder": "Enter amount"}
    )
    
    submit = SubmitField("Save")
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.category_id.choices = _category_choice()
        
class BudgetEditForm(FlaskForm):
    category_id = SelectField(
        "Category",
        coerce=int,
        validators=[DataRequired()],
    )
    
    amount = FloatField(
        "Enter amout($)",
        validators=[DataRequired()],
        render_kw={"placeholder": "Enter amount"}
    )
    
    submit = SubmitField("Update")
    
    def __init__(self, original_category: Budget, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.original_category = original_category
        self.category_id.choices = _category_choice()
        
        if not self.is_submitted():
            if self.original_category.category_id:
                self.category_id.data = original_category.category_id[0].id
            else:
                self.category_id.data = None


class BudgetConfirmDeleteForm(FlaskForm):
    submit = SubmitField("Confirm Delete")