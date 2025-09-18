from django.db import models
from django.utils import timezone

# Create your models here.
class Category(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(null=False, max_length=250)
    display_order = models.IntegerField()
    date_created = models.DateTimeField(default=timezone.now)
