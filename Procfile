release: python manage.py migrate
web: gunicorn mkm_portfolio.wsgi
web: python manage.py collectstatic --no-input; gunicorn myapp.wsgi --log-file - --log-level debug