from django.core.management.base import BaseCommand
from Product.models import Product, Category, Store
from .api_get import Api_get
import requests
from User.models import User
from Favorite.models import Favorites

class Command(BaseCommand):
    help = 'initialize database'

    def handle(self, *args, **kwargs):
        """retrieve a list of products in JSON format through Open Food Fact
        API. The loop goes through each element of the number of pages given,
        checks if the main categories are correctly entered for the product
        and creates a dictionary list."""
        product = Api_get()
        product_list = product.food()
        for i in product_list:
            new_product = Product.objects.create(
                product_name=i["name"],
                brand=i["brand"],
                description=i["description"],
                nutriscore=i["nutriscore"],
                url=i["url"],
            )
            for category in i["category"]:
                """the value of the category key in the dictionary can contain
                several elements. I therefore loop on the category to fill my
                table with get_or_create function of peewee to haven't a
                duplicate"""
                category = category.strip()
                """ strip() remove spaces before and after item"""
                new_category, created = Category.objects.get_or_create(
                    category_name=category)
                id_product = Product.select(Product.unique_id).where(
                    Product.product_name == i["name"]
                )
                id_category = Category.select(Category.unique_id).where(
                    Category.category_name == category
                )
                res = Product_category.insert(
                    product_unique_id=id_product,
                    category_unique_id=id_category).execute()
            """ make a loop for each store"""
            for store in i["store"]:
                """like category, the value of the store key in the dictionary
                can contain several elements. loop to fill my table with the
                get_or_create function"""
                store = store.strip()
                new_store, created = Store.objects.get_or_create(store_name=store)
                id_product = Product.select(Product.unique_id).where(
                    Product.product_name == i["name"]
                )
                id_magasin = Store.select(Store.unique_id).where(
                    Store.store_name == store
                )
                res = Product_store.insert(
                    product_unique_id=id_product, store_unique_id=id_magasin
                ).execute()

        print(product_list)
