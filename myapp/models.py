from django.db import models

# Create your models here.
       
class Asset(models.Model):
    title = models.CharField(max_length=100,default="Untitled Asset")
    status = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def _str_(self):
        return self.Title