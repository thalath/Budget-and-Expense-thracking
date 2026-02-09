from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired, Length
from app.models.expense_budget import Rule

class RuleCreateForm(FlaskForm):
    
    id = StringField(
        "ID *",
        validators=[DataRequired(), Length(min=2, max=10, message="Rule between %(min)d and %(max)d characters.")],
        render_kw={"placeholder": "Enter Rule ID"},
    )
    
    conditions = StringField(
        "Conditions",
        validators=[DataRequired()],
        render_kw={"placeholder": "Enter Conditions"}
    )
    
    conclusion =StringField(
        "Conclusion",
        validators=[DataRequired()],
        render_kw={"placeholder": "Enter Rule Conclusion"}
    )
    
    certainty = FloatField(
        "Certainty",
        validators=[DataRequired()],
        render_kw={"placeholder": "e.g. 0.8"}
    )
    
    explanation = StringField(
        "Explanation",
        validators=[DataRequired()],
        render_kw={"placeholder": "Enter Explanation"}
    )
    
    submit = SubmitField("Save")
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
class RuleEditForm(FlaskForm):
    
    id = StringField(
        "ID *",
        validators=[DataRequired(), Length(min=2, max=10, message="Rule between %(min)d and %(max)d characters.")],
        render_kw={"placeholder": "Enter Rule ID"},
    )
    
    conditions = StringField(
        "Conditions",
        validators=[DataRequired()],
        render_kw={"placeholder": "Enter Conditions"}
    )
    
    conclusion =StringField(
        "Conclusion",
        validators=[DataRequired()],
        render_kw={"placeholder": "Enter Rule Conclusion"}
    )
    
    certainty = FloatField(
        "Certainty",
        validators=[DataRequired()],
        render_kw={"placeholder": "e.g. 0.8"}
    )
    
    explanation = StringField(
        "Explanation",
        validators=[DataRequired()],
        render_kw={"placeholder": "Enter Explanation"}
    )
    
    submit = SubmitField("Update")
    
    def __init__(self, original_rule: Rule, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.original_rule = original_rule
        
class RuleConfirmDeleteForm(FlaskForm):
    sumbit = SubmitField("Confirm Delete")