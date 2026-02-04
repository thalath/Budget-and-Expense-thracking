from flask import Blueprint, render_template, redirect, flash, abort, url_for
from flask_login import login_required
from app.forms.budgets_forms import (
   BudgetCreateForm as BCF,
   BudgetEditForm as BEF,
   BudgetConfirmDeleteForm as BCDF
)
from app.services.budget_service import BudgetService as BS

budget_bp = Blueprint("budgets", __name__, url_prefix="/budgets")

@budget_bp.route("/")
@login_required
def index():
    budgets = BS.get_all_budget()
    return render_template("budgets/index.html", budgets=budgets)

@budget_bp.route("/<int:budget_id>")
@login_required
def detail(budget_id: int):
    budget = BS.get_Budget_by_id(budget_id)
    if budget is None:
        abort(404)
    return render_template("budgets/detail.html", budget=budget)

@budget_bp.route("/create", methods=["GET", "POST"])
@login_required
def create():
    form = BCF()
    if form.is_submitted():
        data = {
            "amount": form.amount.data
        }
        
        category_id = form.category_id.data or None
        
        budget = BS.create_Budget(data, category_id)
        flash(f"Budget '{budget.id}' was create successfully.", "success")
        return redirect(url_for("budgets.index"))
    
    return render_template("budgets/create.html", form=form)

@budget_bp.route("/<int:budget_id>/edit", methods=["GET", "POST"])
@login_required
def edit(budget_id: int):
    budget = BS.get_Budget_by_id(budget_id)
    if budget is None:
        abort(404)
    form = BEF(original_budget=budget, obj=budget)

    if form.validate_on_submit():
        data = {
            "amount": form.amount.data
        }
        category_id = form.category_id.data or None
        
        BS.update_Budget(budget, data, category_id)
        flash(f"Budget: '{budget}' was updated successfully", "success")
        return redirect(url_for("budgets.detail", budget_id=budget.id))

    return render_template("budgets/edit.html", form=form, budget=budget)

@budget_bp.route("/<int:budget_id>/delete", methods=["GET"])
@login_required
def delete_confirm(budget_id):
    budget = BS.get_Budget_by_id(budget_id)
    if budget is None:
        abort(404)
    form = BCDF()
    return render_template("budgets/delete_confirm.html", budget=budget, form=form)


@budget_bp.route("/<int:budget_id>/delte", methods=["POST"])
@login_required
def delete(budget_id:int):
    budget = BS.get_Budget_by_id(budget_id)
    if budget is None:
        abort(404)

    BS.delete(budget)
    flash("Category delete succesfully", "success")
    return redirect(url_for("categories.index"))

