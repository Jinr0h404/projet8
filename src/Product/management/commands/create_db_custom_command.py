from django.core.management.base import BaseCommand
from Product.models import Product
from User.models import User
from Favorite.models import Favorites

class Command(BaseCommand):
    help = 'initialize database'

    def __init__(self):
        self.product_list = []
        self.pages = 5
        self.json = 1
        self.page_size = 50
        self.request_url = "https://fr.openfoodfacts.org/cgi/search.pl"
        self.clean_list = []

    def handle(self, *args, **kwargs):
        """retrieve a list of products in JSON format through Open Food Fact
        API. The loop goes through each element of the number of pages given,
        checks if the main categories are correctly entered for the product
        and creates a dictionary list."""
        for i in range(1, self.pages):
            params = {
                "action": "process",
                "page_size": self.page_size,
                "page": i,
                "json": self.json,
            }
            r = requests.get(self.request_url, params)
            data_json = r.json()
            for product in data_json["products"]:
                if (
                        product.get("product_name_fr")
                        and product.get("categories")
                        and product.get("nutrition_grade_fr")
                        and product.get("stores")
                ):
                    """generate a list of dict where each dict = a product"""
                    for i in self.product_list:
                        if product.get("product_name_fr").lower() not in i["name"]:
                            self.product_list.append(
                                {
                                    "name": product.get("product_name_fr").lower(),
                                    "brand": product.get("brands").lower(),
                                    "store": product.get("stores").lower().split(","),
                                    "category": product.get(
                                        "categories").lower().split(","),
                                    "nutriscore": product.get(
                                        "nutrition_grade_fr").upper(),
                                    "description": product.get("generic_name_fr"),
                                    "url": product.get("url"),
                                }
                            )

    def my_db_setter(self, self.product_list):
        for i in self.product_list:
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