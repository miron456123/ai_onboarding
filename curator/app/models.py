from datetime import datetime
from .db import db

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.String(64), unique=True, nullable=False, index=True)
    title = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(120), nullable=False)
    level = db.Column(db.String(64), nullable=False)
    duration_hours = db.Column(db.Integer, default=0)
    format = db.Column(db.String(64), default='Online')
    language = db.Column(db.String(64), default='Русский')
    description = db.Column(db.Text, default='')
    skills = db.Column(db.JSON, default=list)
    recommended_for = db.Column(db.JSON, default=list)
    prerequisites = db.Column(db.JSON, default=list)
    learning_outcomes = db.Column(db.JSON, default=list)
    difficulty_score = db.Column(db.Integer, default=1)
    estimated_weeks = db.Column(db.Integer, default=1)
    department = db.Column(db.String(120), default='General')
    certificate = db.Column(db.Boolean, default=False)
    rating = db.Column(db.Float, default=0.0)
    tags = db.Column(db.JSON, default=list)

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns if c.name != 'id'}

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False, index=True)
    name = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(120), nullable=False)
    department = db.Column(db.String(120), nullable=False)
    level = db.Column(db.String(64), default='Beginner')
    interests = db.Column(db.JSON, default=list)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id, 'email': self.email, 'name': self.name, 'role': self.role,
            'department': self.department, 'level': self.level, 'interests': self.interests or []
        }

class Enrollment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    status = db.Column(db.String(64), default='planned')
    progress = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    employee = db.relationship('Employee', backref='enrollments')
    course = db.relationship('Course', backref='enrollments')
    __table_args__ = (db.UniqueConstraint('employee_id', 'course_id', name='uq_employee_course'),)
