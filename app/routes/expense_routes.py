from flask import Blueprint, flash, redirect, render_template, url_for, abort
from app.forms.expense_forms import ExpenseCreateForm, ExpenseEditForm, ExpenseConfirmDelete
from app.services.expense_services import ExpenseService
from flask_login import login_required

expense_bp = Blueprint("expenses", __name__, url_prefix="/expenses")

@expense_bp.route("/")
@login_required
def index():
    expenses = ExpenseService.get_all()
    if expenses is None:
        abort(404)
    return render_template("expenses/index.html", expenses=expenses)


@expense_bp.route("/<int:expense_id>")
@login_required
def detail(expense_id: int):
    expense = ExpenseService.get_by_id(expense_id)
    if expense is None:
        abort(404)
    return render_template("expenses/detail.html", expense=expense)


@expense_bp.route("/create", methods=["GET", "POST"])
@login_required
def create():
    form = ExpenseCreateForm()
    if form.validate_on_submit():
        data = {
            "certainty": form.certainty.data,
            "description": form.description.data
        }
        
        category_id = form.categories.data or None
        
        ExpenseService.create(data, category_id)
        flash(f"Expenes '{form.categories}' was created successfully", "success")
        return redirect(url_for("expenses.index"))
    return render_template("expenses/create.html", form=form )


@expense_bp.route("/<int:expense_id>/edit", methods=["GET", "POST"])
@login_required
def edit(expense_id: int):
    expense = ExpenseService.get_by_id(expense_id)
    form = ExpenseEditForm(original_expense=expense, obj=expense)
    if form.validate_on_submit():
        data = {
            "certainty": form.certainty.data or 0.00,
            "description": form.description.data or "-"
        }
        
        category_id = form.categories.data or None
        
        ExpenseService.update(expense=expense,data=data, category_id=category_id)
        flash(f"Expense: '{expense.categories}' was created successfully", "success")
        return redirect(url_for('expenses.index'))
    
    return render_template("expenses/edit.html", expense=expense, form=form)


@expense_bp.route("/<int:expense_id>/delete", methods=["GET"])
@login_required
def delete_confirm(expense_id: int):
    expense = ExpenseService.get_by_id(expense_id)
    if expense is None:
        abort(404)
        
    form = ExpenseConfirmDelete()
    return render_template("expenses/delete_confirm.html", expense=expense, form=form)

@expense_bp.route("/<int:expense_id>/delete", methods=["POST"])
@login_required
def delete(expense_id: int):
    expense = ExpenseService(expense_id)
    if expense is None:
        abort(404)
    
    ExpenseService.delete(expense)
    flash("Expense was Deleted successfully", "success")
    return redirect(url_for('expenses.index'))
        
    