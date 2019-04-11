from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from hello_world.auth import login_required
from hello_world.db import get_db

bp = Blueprint("blog", __name__)


def get_contacts(id, check_author=True):
    """Get a contacts entry from the database, by id."""

    contacts = get_db().execute(
        "SELECT c.id, uses_remaining, owner_id"
        " FROM contacts c JOIN user u on c.owner_id = u.id"
        " WHERE c.id = ?",
        (id,)
    ).fetchone()

    if contacts is None:
        abort(404, "Contacts id {0} doesn't exist".format(id))

    # prevents users from editing others' items
    if check_author and contacts["owner_id"] != g.user["id"]:
        abort(403)

    return contacts


@bp.route("/")
def index():
    """Retrieve the necessary context for the homepage."""
    db = get_db()
    contacts_list = db.execute(
        "SELECT c.id, uses_remaining, created, owner_id, username"
        " FROM contacts c JOIN user u ON c.owner_id = u.id"
        " ORDER BY created DESC",
    ).fetchall()
    return render_template("blog/index.html", contacts_list=contacts_list)


@bp.route("/create", methods=("GET", "POST"))
@login_required
def create():
    """Create a new item"""
    if request.method == "POST":
        uses_remaining = request.form["uses_remaining"]
        error = None

        if not uses_remaining:
            error = "Number of uses is required"

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                "INSERT INTO contacts (uses_remaining, owner_id)"
                " VALUES (?, ?)",
                (uses_remaining, g.user["id"])
            )
            db.commit()

            return redirect(url_for("blog.index"))

    return render_template("blog/create.html")


@bp.route("/<int:id>/update", methods=("GET", "POST"))
@login_required
def update(id):
    """Update a contacts item"""

    contacts = get_contacts(id)

    if request.method == "POST":
        uses = request.form["uses_remaining"]
        error = None

        if not uses:
            error = "Number of uses is required"

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                "UPDATE contacts SET uses_remaining = ?"
                " WHERE id = ?",
                (uses, id)
            )
            db.commit()

            return redirect(url_for("blog.index"))

    return render_template("blog/update.html", contacts=contacts)


@bp.route("/<int:id>/delete", methods=("POST",))
@login_required
def delete(id):
    """Delete a contacts item"""
    get_contacts(id)  # confirms there's contacts with this id
    db = get_db()
    db.execute("DELETE FROM contacts WHERE id = ?", (id,))
    db.commit()

    return redirect(url_for("blog.index"))

