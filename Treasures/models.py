from django.db import models
from django.contrib.auth.models import User

class TreasureGram(models.Model):
    User = models.ForeignKey(User,on_delete=True)
    name = models.CharField(max_length= 50)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    meterial = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    image_url = models.CharField(max_length=500)


    def  __str__(self):
        return self.name