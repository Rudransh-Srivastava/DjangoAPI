from django.db import models

# Create your models here.
class employee(models.Model):
    name = models.CharField(max_length= 23)
    empcode = models.CharField(max_length= 12)
    mobile = models.CharField(max_length=10)
