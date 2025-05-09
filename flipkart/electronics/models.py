from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    image=models.ImageField(upload_to ='',null=True, blank=True)

    def __str__(self):
        return self.name

