from django.db import models

# Create your models here.
class Url(models.Model):
    
    name = models.CharField(max_length=40, blank=False)
    url = models.CharField(max_length=255, blank=False)

class User(models.Model):

    full_name = models.CharField(max_length=20, blank=False)
    email = models.EmailField(blank=False)
    phone_number = models.CharField(blank=False, max_length=12)
    occupation = models.CharField(blank=True, max_length=20)
    password = models.CharField(blank=False)

    def __str__(self):
        return self.full_name

