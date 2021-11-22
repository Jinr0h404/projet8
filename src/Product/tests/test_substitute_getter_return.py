import pytest
from Product.views import substitute_getter
from Product.views import count_to_dict
from Product.models import Product, Category


@pytest.mark.django_db
def test_substitute_getter():
    """test that the function properly sorts the list of product id in descending order of common categories"""
    product_list = [
        {
            "name": "nutella",
            "store": "leclerc",
            "category": ["pate", "pate à tartiner", "petit déjeuner", "chocolat"],
            "nutriscore": "D",
            "description": "petit déjeuner",
            "fat": "0,145",
            "saturated_fat": "0,145",
            "salt": "0,145",
            "sugar": "0,145",
        },
        {
            "name": "lightella",
            "store": "leclerc",
            "category": ["pate"],
            "nutriscore": "B",
            "description": "petit déjeuner",
            "fat": "0,14",
            "saturated_fat": "0,04",
            "salt": "0,02",
            "sugar": "0,14",
        },
        {
            "name": "nutalla",
            "store": "leclerc",
            "category": ["pate à tartiner", "petit déjeuner", "chocolat"],
            "nutriscore": "B",
            "description": "petit déjeuner",
            "fat": "0,14",
            "saturated_fat": "0,04",
            "salt": "0,02",
            "sugar": "0,14",
        },
    ]
    for i in product_list:
        new_product = Product.objects.create(
            product_name=i["name"],
            nutriscore=i["nutriscore"],
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

    id_product = 1
    expected_value = [(3, 3), (2, 1)]
    sut = substitute_getter(id_product)
    assert sut == expected_value


def test_count_to_dict():
    """test that the function indeed creates a dictionary with a set of key id and value counts the number of common categories"""
    product_list = [2, 3, 5, 7, 9, 2, 5, 9, 5, 9, 9]
    expected_value = {2: 2, 3: 1, 5: 3, 7: 1, 9: 4}
    assert count_to_dict(product_list) == expected_value
