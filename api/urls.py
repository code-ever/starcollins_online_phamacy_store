from django.urls import path, include
from . import views


urlpatterns = [
    path('category', views.CategoryView.as_view()),
    path('product', views.ProductView.as_view())
]
