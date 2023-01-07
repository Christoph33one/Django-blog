from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
STATS = ((0, "Draft"), (1,"Published"))


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    # Adding a character field for max 200 characters
