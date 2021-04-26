from django.db import models

# Create your models here.

class Menu(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name

class Categories(models.Model):
    menu = models.ForeignKey('Menu', on_delete = models.CASCADE)
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name

class Products(models.Model):
    category = models.ForeignKey('Categories', on_delete=models.CASCADE)
    korean_name = models.CharField(max_length=45)
    english_name = models.CharField(max_length=45)
    description = models.TextField()
    nutrition = models.ForeignKey("Nutritions", null=True, on_delete=models.SET_NULL)
    allergy = models.ManyToManyField("Allergy", through='AllergyProducts')

    def __str__(self):
        return self.korean_name

class Allergy(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name

class AllergyProducts(models.Model):
    allergy = models.ForeignKey("Allergy", on_delete=models.CASCADE)
    products = models.ForeignKey("Products", on_delete=models.CASCADE)

class Images(models.Model):
    image_url = models.CharField(max_length=2000)
    products = models.ForeignKey("Products", on_delete=models.CASCADE)

class Nutritions(models.Model):
    one_serving_kcal = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    sodium_mg = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    saturated_fat_g = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    sugars_g = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    protein_g = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    caffeine_mg = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    size_ml = models.CharField(max_length=45)
    size_fluid_ounce = models.CharField(max_length=45)