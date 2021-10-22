from django.urls import path
from .views import index, signup

urlpatterns = [
    path('', index, name="user-index"),
    path('signup', signup, name="user-signup")

]