from flask import Blueprint, abort, render_template, redirect, url_for, flash
from extensions import db
from app.services.rule_services import RuleService
from app.forms.rule_forms import RuleCreateForm, RuleEditForm, RuleConfirmDeleteForm

rule_bp = Blueprint("rules", __name__, url_prefix="/rules")

@rule_bp.route("/")
def index():
    rules = RuleService.get_all()
    return render_template("rules/index.html", rules=rules)

@rule_bp.route("<rule_id>")
def detail(rule_id: str):
    rule = RuleService.get_by_id(rule_id)
    if not rule or rule is None:
        abort(404)
    return render_template("rules/detail.html", rule=rule)

@rule_bp.route("/create", methods=["GET", "POST"])
def create():
    form = RuleCreateForm()
    if form.validate_on_submit():
        data = {
            "id": form.id.data,
            "conditions": form.conditions.data,
            "conclusion": form.conclusion.data,
            "certainty": form.certainty.data,
            "explanation": form.explanation.data,
        }
        
        rule = RuleService.create(data)
        flash(f"Rule created successfully", "success")
        return redirect(url_for("rules.index"))
    
    return render_template("rules/create.html", form=form)


@rule_bp.route("/<rule_id>/edit")
def edit(rule_id: str):
    rule = RuleService.get_by_id(rule_id)
    if rule is None or not rule:
        abort(404)

    form = RuleEditForm(original_rule=rule, obj=rule)
    if form.validate_on_submit():
        data = {
            "id": form.id.data,
            "conditions": form.conditions.data,
            "conclusion": form.conclusion.data,
            "certainty": form.certainty.data,
            "explanation": form.explanation.data,
        }
        
        RuleService(rule, data)
        flash(f"Rule {rule.id} updated successfully", "success")
        return redirect(url_for("rules.index"))
    return render_template("rules/edit.html", form=form)

@rule_bp.route("/<rule_id>/delete", methods=["GET"])
def delete_confirm(rule_id: str):
    rule = RuleService.get_by_id(rule_id)
    if rule is None or not rule:
        abort(404)
    form = RuleConfirmDeleteForm()
    return render_template("rules/delete_confirm.html", rule=rule, form=form)

@rule_bp.route("/<rule_id>/delete", methods=["POST"])
def delete(rule_id: str):
    rule = RuleService.get_by_id(rule_id)
    if not rule or rule is None:
        abort(404)

    flash("Rule was Deleted successfully", "succes")
    return redirect(url_for("rules.index"))