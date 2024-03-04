from django.db import models

# Create your models here.


class Products(models.Model):
    name = models.CharField(max_length=30)
    photo = models.ImageField(upload_to='media/productPhoto')
