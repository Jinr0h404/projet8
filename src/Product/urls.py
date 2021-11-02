from django.urls import path
from .views import search, search_substitute, product_info

urlpatterns = [
    path('search', search, name="product-search"),
    path('search_substitute', search_substitute, name="product-search_substitute"),
    path('product_info', product_info, name="product-product_info"),
]