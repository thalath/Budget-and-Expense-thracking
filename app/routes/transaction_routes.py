from flask import Blueprint, render_template, request, redirect, session
from app.models.transaction import Transaction
from extensions import db
from flask_login import login_required

transaction_bp = Blueprint("transaction", __name__, url_prefix="/transaction")

@transaction_bp.route("/")
@login_required
def list_transactions():
    transactions = Transaction.query.filter_by(
        user_id=session["user_id"]
    ).all()
    return render_template("transactions/list.html", transactions=transactions)

@transaction_bp.route("/create", methods=["GET", "POST"])
@login_required
def create_transaction():
    if request.method == "POST":
        t = Transaction(
            amount=request.form["amount"],
            category=request.form["category"],
            type=request.form["type"],
            user_id=session["user_id"]
        )
        db.session.add(t)
        db.session.commit()
        return redirect("/")
    return render_template("transactions/create.html")

@transaction_bp.route("/edit/<int:id>", methods=["GET", "POST"])
@login_required
def edit_transaction(id):
    t = Transaction.query.get(id)
    if request.method == "POST":
        t.amount = request.form["amount"]
        t.category = request.form["category"]
        t.type = request.form["type"]
        db.session.commit()
        return redirect("/")
    return render_template("transactions/edit.html", t=t)

@transaction_bp.route("/delete/<int:id>")
@login_required
def delete_transaction(id):
    t = Transaction.query.get(id)
    db.session.delete(t)
    db.session.commit()
    return redirect("/")
