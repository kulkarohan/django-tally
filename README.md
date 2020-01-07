# django-tally
2019-01-06 This is a Django app.

### Activate virtual enviroment  
(base) PS D:\github\django-tally>  
```pipenv shell```

### Create project  
PS D:\github\django-tally>     
```python C:\Users\guido\.virtualenvs\django-tally-QTYVOJb0\Scripts\django-admin.py startproject tally D:\github\django-tally```

### Configure django-admin.py  
```
import os
## Set the current file path as working directory
SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
TIME_ZONE = 'US/Central'
LANGUAGE_CODE = 'en'
```

### Run Django app  
PS D:\github\django-tally> `python manage.py runserver`
```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 17 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
January 07, 2020 - 01:05:29
Django version 3.0.2, using settings 'tally.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
[07/Jan/2020 01:05:55] "GET / HTTP/1.1" 200 16351
[07/Jan/2020 01:05:55] "GET /static/admin/css/fonts.css HTTP/1.1" 200 423
[07/Jan/2020 01:05:55] "GET /static/admin/fonts/Roboto-Light-webfont.woff HTTP/1.1" 200 85692
[07/Jan/2020 01:05:55] "GET /static/admin/fonts/Roboto-Bold-webfont.woff HTTP/1.1" 200 86184
[07/Jan/2020 01:05:55] "GET /static/admin/fonts/Roboto-Regular-webfont.woff HTTP/1.1" 200 85876
```


