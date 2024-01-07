from django.db import models

# Create your models here.
class Logins(models.Model):
    usernames = models.CharField(max_length=90)
    password = models.CharField(max_length=90)
    user_type = models.CharField(max_length=50)


class Users(models.Model):
    user_id = models.ForeignKey(Logins, on_delete=models.CASCADE)
    name = models.CharField(max_length=90)
    address = models.CharField(max_length=90)
    phone = models.BigIntegerField()


class Products(models.Model):
    name = models.CharField(max_length=90)
    image = models.ImageField(max_length=100)
    price = models.BigIntegerField()
    description = models.CharField(max_length=90)


class Cart(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    date = models.DateField()
    amount =models.IntegerField()


class CartList(models.Model):
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    