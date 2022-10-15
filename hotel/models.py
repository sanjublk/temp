from django.db import models
from django.conf import settings
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location=settings.STATICFILES_DIRS[0])

class Hotel(models.Model):
    name = models.CharField(max_length=30)
    description= models.CharField(max_length=100)
    location= models.CharField(max_length=20)
    type = models.CharField(max_length = 30)
    rating= models.CharField(max_length=10)
    image=models.ImageField(storage=fs)

    def __str__(self):
        return f'<Hotel {self.name}>'