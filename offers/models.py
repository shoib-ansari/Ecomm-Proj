from django.db import models
from django.core.validators import MaxValueValidator


# Create your models here.

class Promocodes(models.Model):
    promo_choices=(
        ('1','Percentage'),
        ('2','Price')
    )
    image = models.ImageField(upload_to="offer_image",blank=True)
    code = models.CharField(max_length=100)
    describtion = models.TextField(max_length=2000)
    min_transaction = models.PositiveIntegerField(default=0)
    max_cashback = models.PositiveIntegerField()
    cashback_type = models.CharField(choices=promo_choices,max_length=1,default=1)
    cashback = models.PositiveIntegerField()
    applicabe_for_transactions = models.IntegerField(default=1)

    def __str__(self):
        return self.code

class Offer(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to="offer_pics")
    discount = models.IntegerField(default=None,validators=[MaxValueValidator(100)])
    end_offer = models.BooleanField(default=False)
    notification = models.CharField(max_length=4000)
    def __str__(self):
        return self.name