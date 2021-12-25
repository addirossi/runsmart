from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()
    discount_price = models.IntegerField()
    image = models.ImageField(upload_to='products')


class Review(models.Model):
    user_name = models.CharField(max_length=50)
    marathons_count = models.IntegerField()
    text = models.TextField()
    user_image = models.ImageField(upload_to='reviews')


class Application(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)