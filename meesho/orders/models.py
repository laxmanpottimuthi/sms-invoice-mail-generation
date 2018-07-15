from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Product(models.Model):
	name = models.CharField(max_length=512)
	created_on = models.DateTimeField(auto_add_now=True)
	is_deleted =models.BooleanField(default=False)



class Order(models.Model):
	created_on = models.DateTimeField(auto_add_now=True)
	is_deleted = models.BooleanField(default=False)
	products = models.ManyToManyField(Product)
	user = models.OneToOneField(User, on_delete=models.CASCADE)


"""User extra info table. Django provides by default user table. This table contains extra information of users"""
class UserInfo(models.Model):
	userid = models.ForeignKey(User, on_delete=models.CASCADE)
	phone_number = models.CharField(max_length=12)