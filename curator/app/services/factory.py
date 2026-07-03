from ..db import db
from ..models import Employee

DEMO_EMPLOYEES = [
    {'email': 'anna@example.com', 'name': 'Анна Смирнова', 'role': 'Product Manager', 'department': 'Product', 'level': 'Intermediate', 'interests': ['Product Management', 'UI/UX']},
    {'email': 'ivan@example.com', 'name': 'Иван Петров', 'role': 'Software Engineer', 'department': 'Engineering', 'level': 'Beginner', 'interests': ['Программирование', 'DevOps']},
    {'email': 'olga@example.com', 'name': 'Ольга Иванова', 'role': 'Data Analyst', 'department': 'Analytics', 'level': 'Advanced', 'interests': ['Аналитика данных', 'SQL']},
]

def seed_demo_employees():
    created = updated = 0
    for payload in DEMO_EMPLOYEES:
        employee = Employee.query.filter_by(email=payload['email']).one_or_none()
        if employee is None:
            db.session.add(Employee(**payload)); created += 1
        else:
            for key, value in payload.items():
                setattr(employee, key, value)
            updated += 1
    db.session.commit()
    return {'created': created, 'updated': updated}
