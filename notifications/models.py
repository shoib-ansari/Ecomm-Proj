from django.db import models
from useraccounts.models import User
from orderprocessing.models import *
# Create your models here.


class Notifications(models.Model):
    product = models.ForeignKey(Ordered_products,on_delete=models.CASCADE,null=True)
    return_request = models.ForeignKey(RerurnRequest,on_delete=models.CASCADE,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)
    notification = models.TextField(max_length=10000,default='Your return request has been approved by us we will contact you soon for return pickup')
    seen_by_user = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)
    link = models.CharField(max_length=400, blank=True)

    def __str__(self):
        return self.title


def save_returnrequest(sender,instance, **kwargs ):
    if instance.approved_for_return == True:
        notifyobj = Notifications.objects.get_or_create(user=instance.user,product=instance.product,return_request=instance)

post_save.connect(save_returnrequest,sender=RerurnRequest)