from django.db import models

# Create your models here.

class Profile(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    email = models.EmailField(unique=True,max_length=200)
    
class Category(models.Model):
    name = models.CharField(max_length=200)
    cart_images = models.ImageField(upload_to='car_images')
    
    def __str__(self):
        return self.name
    
class UploadProduct(models.Model):
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=True, blank=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(max_length=200, blank=True, null=True)
    price = models.TextField(max_length=200, blank=True, null=True)
    quntity = models.IntegerField(default=1)
    
    
    def __str__(self):
        return self.name
    
