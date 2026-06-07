from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):
    # product_to_choose=[
    #    ("Wireless Headphone"),
    #    ("Smartwatch Series 7"),
    #    ("DSLR Camera"),
    #    ("Leather Backpack"),
    #    ("Gaming Laptop"),
    #    ("Bluetooth Speaker"),
    #    ("Modern Sunglasses"),
    #    ("Expresso Machine"),
    # ]

    ##########


    CATEGORY_CHOICES = [
    ('electronics', 'Electronics'),
    ('wooden', 'Wooden'),
    ('clothes', 'Clothes'),
    ]



    ###############

    name=models.CharField(max_length=100)
    price=models.IntegerField(default=0)
    image=models.ImageField(upload_to='products/')
    description = models.TextField(default="No Description")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES) 
    id = models.AutoField(primary_key=True)
    def __str__(self):
        return self.name



class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # def __str__(self):
    #     return self.user

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    # def __str__(self):
    #     return self.product

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    


    # Naya Code - Order save karne ke liye (File ke last mein add karein)
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    city = models.CharField(max_length=50)
    pincode = models.CharField(max_length=10)
    total_amount = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField() # Product ki price order karte time