from django.db import models

# Create your models here.
'''class User(models.Model):
      first_name = models.CharField('Имя', max_length=25)
      last_name = models.CharField('Фамилия', max_length=25)
      username = models.CharField('Название', max_length=120)
      email = models.CharField('Эл. почта', max_length=100)
      phone = models.CharField('Номер телефон', max_length=15)
      password = models.CharField('Пароль', max_length=100)
      created_at = models.DateTimeField('Дата создание')
python -m venv venv
venv\Scripts\.activate.bat
python -m pip install Django
django-admin startproject my_project
cd my_project
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
python manage.py startapp my_app
python manage.py makemigrations
python manage.py migrate
pip install djangorestframework
pip freeze > requirements.txt
pip install -r requirements.txt
python manage.py dumpdata myapp.MyModel --indent 4 > fixtures/my_model.json
python manage.py loaddata fixtures/my_model.json
pip install django-debug-toolbar
Имя пользователя (leave blank to use 'hp'): user
Адрес электронной почты: user@gmail.com
password: qwerty
      class Meta:
            pass
            Abubakr
            turaev1888

            '''


class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    register_at = models.DateTimeField(auto_now_add=True)
    password = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def str(self):
        return self.username

