from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from curator.app import create_app
from curator.app.services.catalog import load_courses

app = create_app()
with app.app_context():
    result = load_courses()
    print(f"Courses loaded: created={result['created']} updated={result['updated']}")
