from django.db import models
from django.contrib.auth.models import User


class Category(models.TextChoices):
    BIDON = "Bidon",
    BALAI = "Balai",
    RACLETTE = "Raclette",
    CHIFFON = "Chiffon",

class Brand(models.TextChoices):
    PRIMA = "Prima", "prima"
    CLEANTEX = "Cleantex", "cleantex"
    PAREX = "Parex", "parex"
    ARIANE = "Ariane", "ariane"



class Product(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=200,blank=False)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    isInStock = models.BooleanField(default=True)
    stock = models.IntegerField(default=0)
    category = models.CharField(max_length=50,choices=Category.choices)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    totalReviewCount = models.IntegerField(default=0)
    createdAt = models.DateTimeField(auto_now_add=True)
    brand = models.CharField(max_length=50,choices=Brand.choices)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    imageUrl = models.URLField(default=None, blank=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    product = models.ForeignKey(Product,null=True,on_delete=models.CASCADE,related_name="reviews")
    user = models.ForeignKey(User, null=True,on_delete=models.SET_NULL)
    rating = models.IntegerField(default=0)
    comment = models.TextField(max_length=1000,default="",blank=False)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment