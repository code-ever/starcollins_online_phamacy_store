from django.contrib import admin
from .models import Profile, Category, UploadProduct
# Register your models here.

admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(UploadProduct)
