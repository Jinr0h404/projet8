from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    """this class is for the django orm, it gives the parameters for the
            creation of the table of the same name in the psql database."""
    username = models.CharField(max_length=200, null=False, verbose_name="Nom")
    email = models.EmailField(max_length=45, unique=True, null=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']