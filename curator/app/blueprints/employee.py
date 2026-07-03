from flask import Blueprint, render_template
from ..services.catalog import list_courses

bp = Blueprint('employee', __name__)

@bp.get('/')
def index():
    return render_template('employee.html', courses=list_courses(limit=12))
