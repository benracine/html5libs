web: python html5libs/manage.py collectstatic --noinput; bin/gunicorn_django -w 4 -b "0.0.0.0:$PORT" html5libs/settings.py
