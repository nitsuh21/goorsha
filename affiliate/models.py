from django.db import models

# Create your models here.
class AffilatePromo(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    url = models.URLField()
    joined_affiliates = models.ManyToManyField('User', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.name