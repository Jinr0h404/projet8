from django.urls import path
from .views import search, search_substitute

urlpatterns = [
    path('search', search, name="product-search"),
    path('search_substitute', search_substitute, name="product-search_substitute"),
]