from django.db import models

# Create your models here.

class studentInfo(models.Model):
    name = models.CharField(max_length=20,null = True,blank=True)
    age = models.IntegerField(max_length=5,null=True,blank=True)
    address = models.TextField()
    def __str__(self):
        return self.name


