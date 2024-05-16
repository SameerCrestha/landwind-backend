from django.db import models

# Create your models here.
class Package(models.Model):
    name=models.CharField(max_length=20)
    desc=models.TextField(max_length=100)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    num_dev=models.CharField(max_length=10)
    prem_support_months=models.PositiveIntegerField()
    free_updates_months=models.PositiveIntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
