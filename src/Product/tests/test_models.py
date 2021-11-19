import pytest
from Product.models import Product, Store, Category


@pytest.mark.django_db
def test_product_model():
    product = Product.objects.create(
        product_name="nutella",
        brand="ferrero",
        description="petit déjeuner",
        nutriscore="D",
        url="http//cici",
        product_image="http//cici",
        product_image_little="http//cici",
        fat="0,145",
        saturated_fat="0,145",
        salt="0,145",
        sugar="0,145",
    )
    expected_value = "nutella"
    assert str(product) == expected_value


@pytest.mark.django_db
def test_category_model():
    category = Category.objects.create(category_name="pate à tartiner")
    expected_value = "pate à tartiner"
    assert str(category) == expected_value


@pytest.mark.django_db
def test_store_model():
    store = Store.objects.create(store_name="auchan")
    expected_value = "auchan"
    assert str(store) == expected_value
