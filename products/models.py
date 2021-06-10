from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class ProductCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Allergen(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    hasPreservatives = models.BooleanField()
    isVegan = models.BooleanField()
    hasAdditives = models.BooleanField()
    allergens = models.ManyToManyField(Allergen)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.CharField(max_length=511)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    on_sale = models.BooleanField()
    ingredients = models.ManyToManyField(Ingredient)

    def __str__(self):
        return self.name + '\n' + self.brand


"""class Allergen_Ingredient(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    allergen = models.ForeignKey(Allergen, on_delete=models.CASCADE)

class Product_Ingredient(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)"""

class ProductImage(models.Model):
    image = models.CharField(max_length=9999)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class ProductReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=511)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField()