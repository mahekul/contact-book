# contact-book
Django Rest Framework for a contact book application

Steps to run 

Install requirement.txt by following command
$ pip install -r requirement.txt

Make the migrations for database model
$ python manage.py makemigrations

Run the migrations
$ python manage.py migrate

Now run the python application
$  export DJANGO_SETTINGS_MODULE=contactbook.settings
$  python manage.py runserver
