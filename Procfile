release: python manage.py migrate
web: python manage.py collectstatic --no-input; gunicorn mkm_portfolio.wsgi --log-file - --log-level debug