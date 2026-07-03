from flask import Blueprint, jsonify, request
from ..models import Course, Employee
from ..services.catalog import list_courses

bp = Blueprint('api', __name__)

@bp.get('/health')
def health():
    return {'status': 'ok'}

@bp.get('/courses')
def courses():
    items = list_courses(category=request.args.get('category'), limit=int(request.args.get('limit', 50)))
    return jsonify([item.to_dict() for item in items])

@bp.get('/employees')
def employees():
    return jsonify([employee.to_dict() for employee in Employee.query.order_by(Employee.name).all()])
