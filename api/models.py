from django.db import models

# Create your models here.
class data(models.Model):
    name = models.CharField(max_length=400)
    email = models.EmailField(max_length=5000)
    article = models.TextField(max_length=100000)


