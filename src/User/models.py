from django.db import models


# Create your models here.
class User(models.Model):
    """this class is for the django orm, it gives the parameters for the
            creation of the table of the same name in the psql database."""
    name = models.CharField(max_length=200, unique=True, null=False, verbose_name="Nom")
    email = models.EmailField(max_length=45, unique=True, null=False)
    password = models.CharField(max_length=45, null=False)