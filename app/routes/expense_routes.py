from flask import Blueprint, render_template, abort, redirect, flash, url_for
from flask_login import login_required
from extensions import db
from app.forms.expense_forms import ExpenseCreateForm as ECF, ExpenseEditForm as EEF, ExpenseConfirmDeleteForm as ECDF
from app.services.expense_service import ExpenseService as ess

expense_bp = Blueprint("expenses", __name__, url_prefix="/expenses")

@expense_bp.route("/")
@login_required
def index():
    expenses = ess.get_all_expense()
    return render_template("expenses/index.html", expenses=expenses)


@expense_bp.route("/<expense_id>")
def detail(expense_id: int):
    expense = ess.get_by_id(expense_id)
    if expense is None:
        abort(404)
    return render_template("expenses/detail.html", expense=expense)

@expense_bp.route("/create", methods=["GET", "POST"])
def create():
    form = ECF()
    if form.validate_on_submit():
        data = {
            "id": form.id.data,
            "amount": form.amount.data
        }
        
        category_id = form.category_id.data or None
        expense = ess.create(data, category_id)
        flash(f"Expense '{expense.amount}' was input successfully", "success")
        return redirect(url_for("expenses.index"))
    
    return render_template("expenses/create.html", form=form)

@expense_bp.route("/<expense_id>/edit", methods=["GET", "POST"])
def edit(expense_id: int):
    expense = ess.get_by_id(expense_id)

    if expense is None:
        abort(404)

    form = EEF(original_expense=expense, obj=expense)

    if form.validate_on_submit():
        data = {
            "id": form.id.data,
            "amount": form.amount.data,
        }
        
        category_id = form.category_id.data or None
        
        ess.update(expense, data, category_id)
        flash(f"Expenses '{expense.categories}' was updated successfully", "success")
        return redirect(url_for("expenses.detail", expense_id= expense.id))

    return render_template("expenses/edit.html", form=form, expense=expense)


@expense_bp.route("/<expense_id>/delete", methods=["GET"])
def delete_confirm(expense_id: int):
    expense = ess.get_by_id(expense_id)
    if expense is None:
        abort(404)
        
    form = ECDF()
    return render_template("expenses/delete_confirm.html", expense=expense, form=form)

    
@expense_bp.route("/expense_id>/delete", methods=["POST"]) # methods post: confirm deleted data from database 
@login_required
def delete(expense_id: int):
    expense = ess.get_by_id(expense_id)
    if expense is None:
        abort(404)

    ess.delete(expense)
    flash("Expense was deleted successfully.", "success")
    return redirect(url_for("expenses.index"))