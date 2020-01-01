from django.db import models
from offers.models import Offer

# Create your models here.

class MainCategory(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name
        
class SubCategory(models.Model):
    main_category = models.ForeignKey(MainCategory,on_delete=models.CASCADE)
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name
        
class FinalCategory(models.Model):
    main_category = models.ForeignKey(MainCategory,on_delete=models.CASCADE)
    sub_category = models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    Main_category = models.ForeignKey(MainCategory,on_delete=models.CASCADE)
    sub_category = models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    Final_category = models.ForeignKey(FinalCategory,on_delete=models.CASCADE)
    Product_Name = models.CharField(max_length=300)
    Price = models.IntegerField(null=True,blank=True)
    Current_Price = models.IntegerField()
    Offer_price = models.IntegerField(null=True,blank=True)
    Description = models.TextField(max_length=5000,blank=True)
    Size = models.CharField(max_length=250,blank=True)
    color = models.CharField(max_length=500,blank=True)
    Total_stock = models.IntegerField(null=True,blank=True)
    Keywords = models.TextField(max_length=2000,blank=True)
    Return_allowed = models.BooleanField(default=True)
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to="Product_Images")
    rating = models.DecimalField(default=0,decimal_places=1,max_digits=5)
    total_ratings = models.IntegerField(default=0)
    offer = models.ForeignKey(Offer,on_delete=models.CASCADE,default=None,null=True,blank=True)


    def __str__(self):
        return self.Product_Name


class Color_variation(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE) 
    color = models.CharField(max_length=100,blank=True)
    Image_one = models.ImageField(upload_to="Product_Images")
    Image_two = models.ImageField(upload_to="Product_Images",blank=True)
    Image_three = models.ImageField(upload_to="Product_Images",blank=True)
    Image_four = models.ImageField(upload_to="Product_Images",blank=True)

class Size_variation(models.Model):
    color = models.ForeignKey(Color_variation,on_delete=models.CASCADE)
    size = models.CharField(max_length=1000,blank=True)
    Quantity = models.CharField(max_length=1000)

    
        