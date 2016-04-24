Django-Truncate
===============

Django-Truncate is a simple library that will add the ability to empty
any given model in any app within your django project, in a more SQL related
words it will **TRUNCATE** the **TABLE** with a simple command::

    python manage.py truncate --apps myapp --models model1 model2

Installation
------------
After you move to your django project main directory follow these simple steps

1. In your terminal/command line run the following command::
        pip install django-truncate

2. Add "django-truncate" to your **INSTALLED_APPS** in the settings.py file::

        INSTALLED_APPS = [
          ...
          'django_truncate',
        ]

3. And that's it! you're now ready to use it.

Usage & Options
---------------
