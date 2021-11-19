import pytest
from django.urls import reverse
from django.test import Client
from Product.models import Product, Category, Store
from pytest_django.asserts import assertTemplateUsed


@pytest.mark.django_db
def test_search_view():
    Product.objects.create(
        product_name="nutella",
        nutriscore="E",
        fat="NC",
        saturated_fat="NC",
        salt="NC",
        sugar="NC",
    )
    client = Client()
    path = reverse("product-search")
    response = client.get(path, {"query": "nutella"})
    assert response.status_code == 200
    assertTemplateUsed(response, "product/search.html")


@pytest.mark.django_db
def test_search_substitute_view():
    product_list = (
        {
            "name": "nutella",
            "brand": "ferrero",
            "store": "leclerc",
            "category": "pate",
            "nutriscore": "D",
            "description": "petit déjeuner",
            "url": "http//cici",
            "product_image": "http//cici",
            "product_image_little": "http//cici",
            "fat": "0,145",
            "saturated_fat": "0,145",
            "salt": "0,145",
            "sugar": "0,145",
        },
        {
            "name": "lightella",
            "brand": "ferreclean",
            "store": "leclerc",
            "category": "pate",
            "nutriscore": "B",
            "description": "petit déjeuner",
            "url": "http//cici",
            "product_image": "http//cici",
            "product_image_little": "http//cici",
            "fat": "0,14",
            "saturated_fat": "0,04",
            "salt": "0,02",
            "sugar": "0,14",
        },
    )
    for i in product_list:
        new_product = Product.objects.create(
            product_name=i["name"],
            brand=i["brand"],
            description=i["description"],
            nutriscore=i["nutriscore"],
            url=i["url"],
            product_image=i["product_image"],
            product_image_little=i["product_image_little"],
            fat=str(i["fat"]),
            saturated_fat=str(i["saturated_fat"]),
            salt=str(i["salt"]),
            sugar=str(i["sugar"]),
        )
        last_product = Product.objects.last()
        prod_id = last_product.pk
        for category in i["category"]:
            """the value of the category key in the dictionary can contain
            several elements. I therefore loop on the category to fill my
            table with get_or_create function of peewee to haven't a
            duplicate"""
            category = category.strip()
            """ strip() remove spaces before and after item"""
            new_category, created = Category.objects.get_or_create(
                category_name=category
            )
            cat_id = new_category.pk
            last_product.category.add(cat_id)
        """ make a loop for each store"""
        for store in i["store"]:
            """like category, the value of the store key in the dictionary
            can contain several elements. loop to fill my table with the
            get_or_create function"""
            store = store.strip()
            new_store, created = Store.objects.get_or_create(store_name=store)
            store_id = new_store.pk
            last_product.store.add(store_id)

    client = Client()
    path = reverse("product-search_substitute")
    response = client.get(path, {"query": 1})
    assert response.status_code == 200
    assertTemplateUsed(response, "product/search_substitute.html")
