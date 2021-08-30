from django.db import models


class Deal(models.Model):
    img = models.ImageField(upload_to='pics')
    country_name = models.CharField(max_length=30)
    city_name = models.CharField(max_length=30)
    title = models.TextField()
    price = models.IntegerField()
    stars = models.IntegerField()