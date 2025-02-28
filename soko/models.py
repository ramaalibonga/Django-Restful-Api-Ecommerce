# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password
from django.db import models
import uuid

class Customer(AbstractUser):
    phone = models.CharField(max_length=15, unique=True, null=True, blank=True)

class Product(models.Model):
    product_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_title = models.CharField(max_length=200)
    product_type = models.CharField(max_length=200)
    product_size = models.CharField(max_length=200)
    product_price = models.DecimalField(max_digits=8,decimal_places=2)
    product_color = models.CharField(max_length=100)
    product_photo = models.ImageField(upload_to="uploads/%Y", height_field=None, width_field=None, max_length=250)
    product_is_sold = models.BooleanField(default=False)
    product_created_at = models.DateTimeField(auto_now_add=True)
    product_created_by = models.ForeignKey(Customer,on_delete=models.CASCADE,related_name="product_customer")


class Order(models.Model):
    order_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order_at = models.DateTimeField(auto_now_add=True)
    order_status = models.BooleanField(default=False)
    order_by = models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    order_product_id = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="order_product")


class Location(models.Model):
    location_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    latitude = models.DecimalField(max_digits=9,decimal_places=7)
    longitude = models.DecimalField(max_digits=9,decimal_places=7)
    location_order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name="location_order")

class Comment(models.Model):
    comment_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    comment_body = models.TextField()
    commented_by = models.ForeignKey(Customer,on_delete=models.CASCADE, null=True,related_name="comment_customer")

class Reply(models.Model):
    reply_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    reply_body = models.TextField()
    reply_by = models.ForeignKey(Customer,on_delete=models.CASCADE, null=True,related_name='reply_customer')
    reply_to = models.ForeignKey(Customer,on_delete=models.CASCADE, null=True,related_name='replies_received')