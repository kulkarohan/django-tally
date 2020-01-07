# django-tally
2019-01-06 This is a Django app.   
[Deploying a Django Application to Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html#w510aac13c37c15c13b7b2b3b3)    


### Activate virtual enviroment  
(base) PS D:\github\django-tally>     
```
pipenv shell
```

### Create project  
PS D:\github\django-tally>     
```
python C:\Users\guido\.virtualenvs\django-tally-QTYVOJb0\Scripts\django-admin.py startproject tally D:\github\django-tally
```
project name: tally  
project directory: D:\github\django-tally  


### Run Django app    
PS D:\github\django-tally>     
```
python manage.py runserver
```   
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

### Configurate settings.py  
```
# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'US/Central' # 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
```
```
# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'OPTIONS': {
                        'options': '-c search_path=django'
                    },
        'NAME': 'postgres',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'database-spotifier.c5eevkz7wazj.us-east-2.rds.amazonaws.com',
        'PORT': '5432',
    },
}
```



