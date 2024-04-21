from django.db import models
from random import choices
from string import ascii_letters
from django.conf import settings

# Create your models here.
class Urlshortner(models.Model):
    original_url = models.URLField()
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
            new_link = self.shortner()
            self.short_url = new_link
            

        return super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.original_url
