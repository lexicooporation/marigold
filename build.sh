#!/usr/bin/env bash
pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
```

**3. `Procfile`** — tells Render how to start your app. Since you have `werkzeug` installed I can see you might have considered Flask at some point, but for Django it should be:
```
web: gunicorn marigoldsite.wsgi:application