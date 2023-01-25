from django.db import models
from django.conf import settings
from random import choices
from string import ascii_letters
# Create your models here.

class Link(models.Model):
    original_link=models.URLField()
    shortened_link=models.URLField(blank=True,null=True)

    def shortener(self):
        while True:
            random_string=''.join(choices(ascii_letters,k=6))
            new_link=settings.HOST_URL+'/'+random_string
    
            if not Link.objects.filter(shortened_link=new_link).exists():
                break

        return new_link

class User(models.Model):

    full_name = models.CharField(max_length=20, blank=False)
    email = models.EmailField(blank=False)
    phone_number = models.CharField(blank=False, max_length=12)
    occupation = models.CharField(blank=True, max_length=20)
    password = models.CharField(blank=False, max_length=15)

    def __str__(self):
        return self.full_name

