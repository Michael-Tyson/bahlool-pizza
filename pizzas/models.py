from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Pizza(models.Model):
    """have some pizza names"""
    name=models.CharField(max_length=100)
    fucking_owner=models.ForeignKey(User,on_delete=models.CASCADE)
    class Meta():
        verbose_name_plural="Pizzas"
    def __str__(self):
        return self.name.title()
    

class Toppings(models.Model):
    """add related toppings to specific pizzas"""
    pizza=models.ForeignKey(Pizza,on_delete=models.CASCADE)
    name=models.TextField()
    def __str__(self):
        return self.name.title()
