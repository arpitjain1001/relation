from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=30)
    age= models.IntegerField()
    email = models.EmailField()
    address= models.TextField()
    # image = models.ImageField()
    # file= models.FileField()

# 1)makemigrations: which is responsible for creating new migrations based on the changes you have made to your models.
# 2)migrate: which is responsible for applying and unapplying migrations.
