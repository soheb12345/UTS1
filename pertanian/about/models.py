from django.db import models

# Create your models here.
class user(models.Model):
    id = models.IntegerField(primary_key=true)
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=255)
    price = models.IntegerField()