from flask import Blueprint, render_template
from ..models import Course, Employee

bp = Blueprint('admin', __name__)

@bp.get('/')
def index():
    return render_template('admin.html', course_count=Course.query.count(), employee_count=Employee.query.count())
