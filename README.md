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
cd C:\Users\guido\.virtualenvs\django-tally-QTYVOJb0\Scripts\
python django-admin.py startproject tally D:\github\django-tally
```
project (app) name: tally  
project created in directory: D:\github\django-tally   


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
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'OPTIONS': {
                        'options': '-c search_path=django'
                    },
        'NAME': 'postgres',
        'USER': '***',
        'PASSWORD': '***',
        'HOST': '***',
        'PORT': '5432',
    },
}
```
Migrate Django admin tables to database `django` schema.   

### Migration   
```
cd d:/github/django-tally
```
PS D:\github\django-tally> 
```
python manage.py migrate
```
```
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying sessions.0001_initial... OK
```



