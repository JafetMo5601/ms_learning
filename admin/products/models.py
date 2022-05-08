from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    image = models.CharField(max_length=250)
    likes = models.PositiveIntegerField(default=0)

class User(models.Model):
    username = models.CharField(max_length=20)
    user_id =models.CharField(max_length=15, unique=True, default='')
    name = models.CharField(max_length=20)
    last = models.CharField(max_length=20)