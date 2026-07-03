from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from curator.app import create_app
from curator.app.db import db
from curator.app.services.catalog import load_courses
from curator.app.services.factory import seed_demo_employees

app = create_app()
with app.app_context():
    db.create_all()
    courses = load_courses()
    employees = seed_demo_employees()
    print(f"Database initialized: courses created={courses['created']} updated={courses['updated']}; demo employees created={employees['created']} updated={employees['updated']}")
