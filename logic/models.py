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

class Campaign(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    business = models.ForeignKey(Business, on_delete=models.CASCADE,related_name='business')
    affiliates = models.ForeignKey(User, on_delete=models.CASCADE, related_name='affiliates')

    def __str__(self):
        return self.name

