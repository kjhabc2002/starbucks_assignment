from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
          db_table = 'menus'

class Category(models.Model):
    name = models.CharField(max_length=20)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)

    class Meta:
          db_table = 'categories'

class Product(models.Model): 
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    class Meta:
        db_table = 'products'

class ProductAllergy(models.Model):
    allergy = models.ForeignKey('Allergy', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    class Meta:
        db_table = 'product_allergies'


class Allergy(models.Model):
    name = models.CharField(max_length=50)
    products = models.ManyToManyField('Product', through='ProductAllergy')
    class Meta:
        db_table = 'allergies'

class Nutrition(models.Model):
    one_serving_kcal = models.DecimalField(max_digits=10, decimal_places=2)
    sodium_mg = models.DecimalField(max_digits=10, decimal_places=2)
    saturated_fat_g = models.DecimalField(max_digits=10, decimal_places=2)
    sugars_g = models.DecimalField(max_digits=10, decimal_places=2)
    protein_g = models.DecimalField(max_digits=10, decimal_places=2)
    caffeine_mg = models.DecimalField(max_digits=10, decimal_places=2)
    product = models.OneToOneField('Product', on_delete=models.CASCADE)

    class Meta:
        db_table = 'nutritions'

class Image(models.Model):
    image_url = models.URLField(max_length=2000)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    class Meta:
        db_table = 'images'


