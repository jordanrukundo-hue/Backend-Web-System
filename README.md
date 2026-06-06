# 1. Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure environment
cp .env.example .env
# Edit .env with your values (leave DATABASE_URL empty for SQLite)

# 4. Run migrations
python manage.py migrate

# 5. Create superuser (admin)
python manage.py createsuperuser

# 6. Start server
python manage.py runserver
