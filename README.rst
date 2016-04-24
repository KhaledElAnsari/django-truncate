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

1. You can truncate all of the tables in one app or multiple apps using **--apps**::

        python manage.py truncate --apps appone apptwo

2. If you want you can truncate a specific table(s) in an app using **--models**::

        python manage.py truncate --apps appone --models Model3

   Note if you don't write the name of the app the truncate will stop and you'll see an error message in the terminal

Remember you can always see the instructions by running::

    python manage.py truncate -h

License
-------

This project is under the BSD License.
