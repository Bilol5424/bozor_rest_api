from django.db import models

# Create your models here.

class User(models.Model):
      id = models.AutoField(primary_key=True)
      first_name = models.CharField('Имя', max_length=25)
      last_name = models.CharField('Фамилия', max_length=25)
      username = models.CharField('Название', max_length=120)
      email = models.CharField('Эл. почта', max_length=100)
      phone = models.CharField('Номер телефон', max_length=15)
      password = models.CharField('Пароль', max_length=100)
      created_at = models.DateTimeField('Дата создание')

      class Meta:
            pass
      

      