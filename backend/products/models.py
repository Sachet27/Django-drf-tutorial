from django.db import models

# Create your models here.
class Product(models.Model):
    title= models.CharField(max_length=128, blank=False, null= False) 
    content= models.TextField(blank= True)
    price= models.DecimalField(max_digits= 15, decimal_places= 2)

    def __str__(self):
        return self.title