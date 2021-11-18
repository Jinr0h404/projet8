import pytest
from django.test import Client
from Favorite.models import Favorites
from Product.models import Product, Store, Category
from User.models import CustomUser


@pytest.mark.django_db
def test_custom_user_model():
    client = Client()
    username = 'test_user'
    email = "troubadour@gmail.com"
    password = 'Troubadour'
    user = CustomUser.objects.create_user(username=username, email=email, password=password)
    expected_value = "test_user | troubadour@gmail.com"
    assert str(user) == expected_value