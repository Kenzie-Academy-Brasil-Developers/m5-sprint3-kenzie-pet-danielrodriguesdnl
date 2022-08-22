from django.db import models

# Create your models here.
class Trait(models.Model):
    name = models.CharField(max_length=20, unique=True)

    animal = models.ForeignKey("animals.Animal", on_delete=models.CASCADE, related_name='traits', null=True)

    