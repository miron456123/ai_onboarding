from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from curator.app import create_app
from curator.app.services.factory import seed_demo_employees

app = create_app()
with app.app_context():
    result = seed_demo_employees()
    print(f"Demo employees loaded: created={result['created']} updated={result['updated']}")
