# AI Onboarding Curator

Локальное Flask-приложение для подбора и администрирования курсов онбординга.

## Минимальный запуск без Docker

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python scripts/init_db.py
flask --app run.py run --debug
```

По умолчанию используется SQLite:

```env
DATABASE_URL=sqlite:///curator.db
```

PostgreSQL по-прежнему поддерживается через переменную окружения:

```env
DATABASE_URL=postgresql+psycopg://curator:curator@localhost:5432/curator
```

## Запуск через Flask-Migrate

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
flask --app run.py db upgrade
python curator/scripts/seed_courses.py
python curator/scripts/seed_demo.py
flask --app run.py run --debug
```

## Инициализация без Alembic

```bash
python scripts/init_db.py
```

Команда идемпотентно создает таблицы через `db.create_all()`, загружает каталог курсов и демо-сотрудников.

## Проверка

```bash
pytest
```
