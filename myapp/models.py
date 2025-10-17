from django.db import models

# Create your models here.
       
class Asset(models.Model):
    title = models.CharField(max_length=100) 
    status = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title