from django.db import models
from users.models import User

# Create your models here.
class Business(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=0)
    image = models.ImageField(upload_to='product_images/')
    published_by = models.ForeignKey(Business, on_delete=models.CASCADE,related_name='business')

    def __str__(self):
        return self.name


class Campaign(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='product')
    business = models.ForeignKey(Business, on_delete=models.CASCADE,related_name='business')
    affiliates = models.ForeignKey(User, on_delete=models.CASCADE, related_name='affiliates')
    no_of_likes = models.IntegerField(blank=True)
    no_of_visitors = models.IntegerField(blank=True)
    no_of_sales = models.IntegerField(blank=True)

    def __str__(self):
        return self.name