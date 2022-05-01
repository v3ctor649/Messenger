from django.db import models
# Create your models here.


class Messages(models.Model):
    name = models.TextField()
    message = models.TextField()