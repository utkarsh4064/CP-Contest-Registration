import email
from django.db import models

class Home(models.Model):
    name= models.CharField(max_length=100)
    email= models.EmailField()
    rating= models.IntegerField()
    other= models.TextField()
    date=models.DateField()
    def __str__(self):
        return self.name