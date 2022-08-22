from django.db import models

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=20, unique=True)
    scientific_name = models.CharField (max_length=50, unique=True)



    animal = models.OneToOneField("animals.Animal", on_delete=models.CASCADE)