from django.db import models
from useraccounts.models import User
from django.db.models.signals import post_save
from offers.models import Promocodes
from products.models import Product

# Create your models here.



class Checkout(models.Model):

    STATUS_CHOICES = (
        (1, "Placed by user"),
        (2, "seen"),
        (3, "delivered"),
        (4, "approved by User"),
        (5, "In Return request")
    )
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
    status = models.IntegerField(choices=STATUS_CHOICES,default=1)
    promocode = models.ForeignKey(Promocodes,on_delete=models.CASCADE,null=True)


    def __str__(self):
        return  self.c_name

class Ordered_products(models.Model):
    checkout = models.ForeignKey(Checkout,on_delete=models.CASCADE)
    product= models.ForeignKey(Product,on_delete=models.CASCADE)
    color = models.CharField(max_length=200)
    quantity = models.IntegerField()
    Image = models.ImageField(max_length=400)
    sell_price = models.IntegerField()
    price = models.IntegerField()


# class RerurnRequest(models.Model):
#     user = models.ForeignKey(User,on_delete=models.CASCADE)
#     checkout = models.ForeignKey(Checkout,on_delete=models.CASCADE)
#     feedback = models.TextField(max_length=90000)
#     seen_status = models.BooleanField(default=False)
#     approved_for_return = models.BooleanField(default=False)
#     return_status = models.BooleanField(default=False)

#     def __str__(self):
#         return self.user.username

# class Notifications(models.Model):
#     checkout = models.ForeignKey(Checkout,on_delete=models.CASCADE,null=True)
#     return_request = models.ForeignKey(RerurnRequest,on_delete=models.CASCADE,null=True)
#     user = models.ForeignKey(User,on_delete=models.CASCADE)
#     title = models.CharField(max_length=1000)
#     notification = models.TextField(max_length=10000,default='Your return request has been approved by us we will contact you soon for return pickup')
#     seen_by_user = models.BooleanField(default=False)
#     date = models.DateField(auto_now_add=True)
#     link = models.CharField(max_length=400, blank=True)


#     def __str__(self):
#         return self.user.username

# def save_returnrequest(sender,instance, **kwargs ):
#     if instance.approved_for_return == True:
#         notifyobj = Notifications.objects.get_or_create(user=instance.user,checkout=instance.checkout,return_request=instance)


# post_save.connect(save_returnrequest,sender=RerurnRequest)