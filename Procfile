web: python html5libs/manage.py collectstatic --noinput; python html5libs/manage.py run_gunicorn -w 4 -b "0.0.0.0:$PORT" html5libs/settings.py
