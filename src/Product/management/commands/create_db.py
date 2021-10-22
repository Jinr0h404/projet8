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
                    category_name=category)
                print("attention la première categorie est enregistrée")
                print(prod_id, 'est identifiant du prduit')
                print("on passe à l'id category")
                last_category = Category.objects.last()
                cat_id = last_category.pk
                last_product.category.add(
                    cat_id)
                print("j'ai bien ajouté ma catégorie avec mon produit dans la table d'association")
            """ make a loop for each store"""
            for store in i["store"]:
                """like category, the value of the store key in the dictionary
                can contain several elements. loop to fill my table with the
                get_or_create function"""
                store = store.strip()
                new_store, created = Store.objects.get_or_create(store_name=store)
                last_store = Store.objects.last()
                store_id = last_store.pk
                last_product.store.add(
                    store_id)
                print("j'ai bien ajouté mon magasin avec mon produit dans la table d'association")
