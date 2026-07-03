from curator.app import create_app
from curator.app.models import Course, Employee, Enrollment

app = create_app()

__all__ = ['app', 'Course', 'Employee', 'Enrollment']
