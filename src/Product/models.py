from django.db import models


# Create your models here.
class Product(models.Model):
    """this class is for the django orm, it gives the parameters for the
        creation of the table of the same name in the psql database."""
    product_name = models.CharField(max_length=200, unique=True, verbose_name="Produit")
    brand = models.TextField(null=True, verbose_name="Marque")
    description = models.TextField(null=True)
    nutriscore = models.CharField(max_length=1)
    url = models.URLField(null=True)
    category = models.ManyToManyField(Category)
    store = models.ManyToManyField(Store)


class Store(models.Model):
    store_name = models.CharField(max_length=100, unique=True, verbose_name="Magasin")


class Category(models.Model):
    category_name = models.CharField(max_length=200, unique=True, verbose_name="Catégorie")
