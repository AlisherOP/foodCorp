#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mylist.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()


# FOR ME:
# PS C:\My docs\Web app\back\mylist> python3 manage.py runserver
# python manage.py migrate= creats the nessessery migrations
# to apply the changes that we did; python manage.py makemigrations food
#                                                              food= is app that had this changes
# then: python manage.py sqlmigrate food 0002(may depend on the number)
#lastly: python migrate



# to creat an actual table
# Migrations for 'food':
#   food\migrations\0001_initial.py
#     - Create model Item
# PS C:\My docs\Web app\back\mylist> python manage.py sqlmigrate food 0001



# python manage.py createsuperuser
# t00rsh04, user:tursh, gmail: tursh04


#making an envirnment: source myenv/bin/activate

#9-4