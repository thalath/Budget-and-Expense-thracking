from flask import Blueprint, render_template, redirect, flash, abort, url_for
from flask_login import login_required
from app.forms.category_forms import (
    CategoryCreateForm as CCF,
    CategoryEditForm as CEF,
    CategoryConFirmDeleteForm as CDF
)
from app.services.category_service import CategoryService as CS

category_bp = Blueprint("categories", __name__, url_prefix="/categories")

@category_bp.route("/")
@login_required
def index():
    categories = CS.get_all_category()
    return render_template("categories/index.html", categories=categories)

@category_bp.route("/<int:category_id>")
@login_required
def detail(category_id: int):
    category = CS.get_category_by_id(category_id)
    if category is None:
        abort(404)
    return render_template("categories/detail.html", category=category)

@category_bp.route("/create", methods=["GET", "POST"])
@login_required
def create():
    form =CCF()
    if form.is_submitted():
        data = {
            "name": form.name.data
        }
        
        category = CS.create_category(data)
        flash(f"Category '{category.name}' was create successfully.", "success")
        return redirect(url_for("categories.index"))
    
    return render_template("categories/create.html", form=form)

@category_bp.route("/<int:category_id>/edit", methods=["GET", "POST"])
@login_required
def edit(category_id:int):
    category = CS.get_category_by_id(category_id)
    if category is None:
        abort(404)
    form = CEF(original_category=category, obj=category)

    if form.validate_on_submit():
        data = {
            "name": form.name.data
        }
        CS.update_category(category, data)
        flash(f"Category: '{category}' was updated successfully", "success")
        return redirect(url_for("categories.detail", category_id=category.id))

    return render_template("categories/edit.html", form=form, category=category)

@category_bp.route("/<int:category_id>/delete", methods=["GET"])
@login_required
def delete_confirm(category_id):
    category = CS.get_category_by_id(category_id)
    if category is None:
        abort(404)
    form = CDF()
    return render_template("categories/delete_confirm.html", categories=category, form=form)


@category_bp.route("/<int:category_id>/delte", methods=["POST"])
@login_required
def delete(category_id:int):
    category = CS.get_category_by_id(category_id)
    if category is None:
        abort(404)

    CS.delete(category)
    flash("Category delete succesfully", "success")
    return redirect(url_for("categories.index"))

