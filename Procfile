web: python html5libs/manage.py run_gunicorn -b "0.0.0.0:$PORT" -w 3
web: python html5libs/manage.py collectstatic --noinput; bin/gunicorn_django --workers=3 --bind=0.0.0.0:$PORT html5libs/settings.py 
