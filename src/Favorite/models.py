from django.db import models
from Product.models import Product
from User.models import User

# Create your models here.
class Favorites(models.Model):
    """this class is for the django orm, it gives the parameters for the
            creation of the table of the same name in the psql database."""
    substitute_id = models.ForeignKey(Product, on_delete=models.RESTRICT, verbose_name="Substitut")
    product_id = models.ForeignKey(Product, on_delete=models.RESTRICT, related_name="bad_product", verbose_name="Produit ")
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Utilisateur")