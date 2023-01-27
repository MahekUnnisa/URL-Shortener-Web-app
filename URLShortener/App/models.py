from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone
from random import choices

from string import ascii_letters

# Model/Table to store the links
class Link(models.Model):
    original_link=models.URLField()
    shortened_link=models.URLField(blank=True,null=True)

    custom_string = models.CharField(max_length=15)
    click_count = models.IntegerField(default=0)

    expiration_date = models.DateTimeField(default=timezone.now() + timezone.timedelta(days=7))
    created_at = models.DateTimeField(auto_now_add=True)

    # Shorten the URL
    def shortener(self):
        while True:
            random_string=''.join(choices(ascii_letters,k=6))
            
            new_link=settings.HOST_URL+'/'+self.custom_string+'/'+random_string
    
            if not Link.objects.filter(shortened_link=new_link).exists():
                break

        return new_link

    # Save the URL in the DB
    def save(self,*args, **kwargs):
        if not self.shortened_link:
            new_link=self.shortener()
            self.shortened_link=new_link
        return super().save(*args, **kwargs)

    # Check if the link is expired
    def is_expired(self):
        return self.expiration_date < timezone.now()
        
    # View link in Django Admin panel
    def __str__(self):
        return self.shortened_link


