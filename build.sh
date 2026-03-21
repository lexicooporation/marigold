#!/usr/bin/env bash
set -e

pip install -r requirements.txt
cd marigoldsite
python manage.py collectstatic --no-input
python manage.py migrate
```

**Third, fix your Render start command** to:
```
cd marigoldsite && gunicorn marigoldsite.wsgi:application