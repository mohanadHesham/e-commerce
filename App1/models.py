from django.db import models
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField()
    price = models.DecimalField(max_digits=11,decimal_places=2)
    category_id = models.ForeignKey(Category,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

