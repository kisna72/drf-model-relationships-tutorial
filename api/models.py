from django.db import models
from django.contrib import admin

# Create your models here.
# Product Ingredient
class Product(models.Model):
    name = models.TextField()
    
    def __str__(self):
        return self.name

class Ingredient(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE, related_name="ingredients",)
    protein = models.FloatField()
    carb = models.FloatField()
    fat = models.FloatField()

    def __str__(self):
        return self.product.name

admin.site.register(Product)
admin.site.register(Ingredient)