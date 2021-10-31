from django.db import models


# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=200, unique=True, verbose_name="Catégorie")


class Store(models.Model):
    store_name = models.CharField(max_length=100, unique=True, verbose_name="Magasin")


class Product(models.Model):
    """this class is for the django orm, it gives the parameters for the
        creation of the table of the same name in the psql database."""
    product_name = models.CharField(max_length=200, verbose_name="Produit")
    product_image = models.URLField(null=True)
    brand = models.TextField(null=True, verbose_name="Marque")
    description = models.TextField(null=True)
    nutriscore = models.CharField(max_length=1)
    #fat = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    fat = models.CharField(max_length=30, default='NC')
    saturated_fat = models.CharField(max_length=30, default='NC')
    salt = models.CharField(max_length=30, default='NC')
    sugar = models.CharField(max_length=30, default='NC')
    url = models.URLField(null=True)
    category = models.ManyToManyField(Category)
    store = models.ManyToManyField(Store)

