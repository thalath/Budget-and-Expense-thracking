from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class CategoryCreateForm(FlaskForm):
    name = StringField(
        "Category name",
        validators=[DataRequired(), Length(min=3, max=100)],
        render_kw={"placeholder": "Enter categories Name. e.g. Food"}
    )
    
    submit = SubmitField("Save")
    
class CategoryEditForm(FlaskForm):
    name = StringField(
        "Category Name",
        validators=[DataRequired()],
        render_kw={"placeholder": "Enter category Name. e.g. Food"}
    )
    
    submit = SubmitField("Update")
    
class CategoryConFirmDeleteForm(FlaskForm):
    submit = SubmitField("Confirm Delete")