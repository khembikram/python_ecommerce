from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('products/', views.getProducts, name="Products"),
    path('products/<str:pk>/', views.getProduct, name="Product"),
]