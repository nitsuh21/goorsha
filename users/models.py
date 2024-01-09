from django.db import models

# Create your models here.
class User(models.AbstractUser):
    firstname = models.CharField(max_length=50)
    middlename = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=50)
    phonenumber = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    profile_picture = models.ImageField(upload_to='profile_pictures', blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    own_businesses = models.BooleanField(default=False)
    business = models.ForeignKey('Business', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.username

class Business(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Campaign(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    affiliates = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name