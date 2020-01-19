from django.db import models
from useraccounts.models import User
from django.db.models.signals import post_save
from offers.models import Promocodes
from products.models import Product

# Create your models here.



class Checkout(models.Model):
    Mark_as_seen = models.BooleanField(default=0)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    first_name = models.TextField(max_length=400,blank=False)
    last_name = models.TextField(max_length=400,blank=False)
    number = models.BigIntegerField()
    alt_number = models.BigIntegerField()
    pincode = models.IntegerField()
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=1500)
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    payment_option = models.CharField(max_length=60,default=None,null=True)
    delivered = models.BooleanField(default=0)
    promocode = models.ForeignKey(Promocodes,on_delete=models.CASCADE,null=True)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return  self.first_name

class Ordered_products(models.Model):

    STATUS_CHOICES = (
        (1, "Placed by user"),
        (2, "seen"),
        (3, "delivered"),
        (4, "approved by User"),
        (5, "In Return request")
    )

    checkout = models.ForeignKey(Checkout,on_delete=models.CASCADE)
    product= models.ForeignKey(Product,on_delete=models.CASCADE)
    color = models.CharField(max_length=200)
    quantity = models.IntegerField()
    Image = models.ImageField(max_length=400)
    sell_price = models.IntegerField()
    price = models.IntegerField()
    size = models.CharField(max_length=80)
    status = models.IntegerField(choices=STATUS_CHOICES,default=1)

    # def __str__(self):
    #     return  self.product


class RerurnRequest(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Ordered_products,on_delete=models.CASCADE)
    feedback = models.TextField(max_length=90000)
    seen_status = models.BooleanField(default=False)
    approved_for_return = models.BooleanField(default=False)
    return_status = models.BooleanField(default=False)


