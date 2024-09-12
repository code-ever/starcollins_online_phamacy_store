from rest_framework import serializers
from .models import Profile,UploadProduct, Category

class UploadSerializer(serializers.ModelSerializer):
    class Meta:
      model = UploadProduct
      fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        