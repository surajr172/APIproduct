from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Product(models.Model):
    pname = models.CharField(max_length = 20)
    pprice = models.IntegerField(blank= False,default='0')
    description = models.CharField(max_length=50)

    def __str___(self):
        return self.pname