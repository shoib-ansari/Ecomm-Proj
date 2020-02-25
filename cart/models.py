from django.db import models
from useraccounts.models import User
from products.models import Product
from useraccounts.models import User
from products.models import Color_variation

# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    Quantity = models.IntegerField(default=0)
    size = models.CharField(max_length=100)
    color = models.ForeignKey(Color_variation,on_delete=models.CASCADE)

class Wishlist(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)


