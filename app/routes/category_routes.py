from flask import flash, redirect, render_template, Blueprint, abort, url_for
from flask_login import login_required
from app.services.category_services import CategoryService
from app.forms.category_forms import CategoryCreateForm, CategoryEditForm, CategoryConfirmDelete

category_bp = Blueprint("categories", __name__, url_prefix="/categories")

@category_bp.route("/")
@login_required
def index():
    categories = CategoryService.get_all()
    if categories is None:
        abort(404)
    return render_template("categories/index.html", categories=categories)


@category_bp.route("/<int:category_id>")
@login_required
def detail(category_id: int):
    category = CategoryService.get_by_id(category_id)
    if category is None:
        abort(404)
    return render_template("categories/detail.html", category=category)

@category_bp.route("/create", methods=["GET", "POST"])
@login_required
def create():
    form = CategoryCreateForm()
    if form.validate_on_submit():
        data = {
            "name": form.name.data,
            "description": form.description.data
        }
        
        category = CategoryService.create(data)
        flash(f"Category: '{category.name}' was create successfully", "success")
        return redirect(url_for("categories.index"))

    return render_template("categories/create.html", form=form)

@category_bp.route("/<int:category_id>/edit", methods=["GET", "POST"])
@login_required
def edit(category_id: int):
    category = CategoryService.get_by_id(category_id)
    
    if category is None:
        abort(404)
    
    form = CategoryEditForm(original_category=category, obj=category)
    if form.validate_on_submit():
        data = {
            "name": form.name.data,
            "description": form.description.data
        }
        CategoryService.update(category, data)
        flash(f"Category '{category.name}'", "success")
        return redirect(url_for('categories.index'))

    return render_template("categories/edit.html", category=category, form=form)

@category_bp.route("/<int:category_id>/delete", methods=["GET"])
@login_required
def delete_confirm(category_id: int):
    category = CategoryService.get_by_id(category_id)
    if category is None:
        abort(404)
    form = CategoryConfirmDelete()
    return render_template("categories/delete_confirm.html",category=category, form=form, )

@category_bp.route("/<int:category_id>/delete", methods=["POST"])
@login_required
def delete(category_id: int):
    category = CategoryService.get_by_id(category_id)
    if category is None:
        abort(404)
    form = CategoryService.delete(category)
    flash("Category deleted successfully", "success")

    return redirect(url_for('categories.index'))