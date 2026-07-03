import json
from pathlib import Path
from ..db import db
from ..models import Course

COURSE_FIELDS = {c.name for c in Course.__table__.columns if c.name != 'id'}

def load_courses(path=None):
    path = Path(path or Path(__file__).resolve().parents[2] / 'data' / 'courses.jsonl')
    created = updated = 0
    with path.open(encoding='utf-8') as fh:
        for line in fh:
            if not line.strip():
                continue
            payload = {k: v for k, v in json.loads(line).items() if k in COURSE_FIELDS}
            course = Course.query.filter_by(course_id=payload['course_id']).one_or_none()
            if course is None:
                db.session.add(Course(**payload)); created += 1
            else:
                for key, value in payload.items():
                    setattr(course, key, value)
                updated += 1
    db.session.commit()
    return {'created': created, 'updated': updated}

def list_courses(category=None, limit=50):
    query = Course.query
    if category:
        query = query.filter(Course.category == category)
    return query.order_by(Course.rating.desc(), Course.title).limit(limit).all()
