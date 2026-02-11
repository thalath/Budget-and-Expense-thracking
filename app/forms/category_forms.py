from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length
from app.models.categories import Category

class CategoryCreateForm(FlaskForm):
    name = StringField(
        "Name *",
        validators=[DataRequired(), Length(min=2, max=15)],
        render_kw={"placeholder": "Enter category name"}
    )
    
    description = TextAreaField(
        "Description",
        validators=[DataRequired()],
        render_kw={"placeholder": "Description"}
    )
    
    submit = SubmitField("Save")

class CategoryEditForm(FlaskForm):
    name = StringField(
        "Name*",
        validators=[DataRequired()],
        render_kw={"placeholder": "Enter category name"}
    )
    
    description = TextAreaField(
        "Description",
        validators=[DataRequired()]
    )
    
    submit = SubmitField("Update")
    
    def __init__(self, original_category: Category, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.original_category = original_category
        
        
class CategoryConfirmDelete(FlaskForm):
    submit = SubmitField("Confirm Delete")