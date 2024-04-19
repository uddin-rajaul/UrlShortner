from operator import truediv
from django.db import models
from random import choices
from string import ascii_letters
from django.conf import settings

# Create your models here.
class Urlshortner(models.Model):
    original_url = models.URLField(unique=True)
    short_url = models.URLField(blank=True, null=True)

    def shortner(self):
        while True:
            random_strings = ''.join(choices(ascii_letters, k=6))
            new_link = settings.HOST_URL+"/"+random_strings
            if not Urlshortner.objects.filter(short_url=new_link).exists():
                break
        
        return new_link
    
    def save(self, *args, **kwargs):
        if not self.short_url:
            if Urlshortner.objects.filter(original_url=self.original_url).exists():
                url_exists = Urlshortner.objects.get(original_url=self.original_url).short_url
                self.short_url = url_exists
            else:
                new_link = self.shortner()
                self.short_url = new_link

        return super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.original_url



