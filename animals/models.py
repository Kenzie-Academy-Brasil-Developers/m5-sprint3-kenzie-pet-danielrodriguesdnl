from django.db import models

# Create your models here.
class SexAnimal(models.TextChoices):
    MALE = "Macho"
    FEMALE = "Femea"
    DEFAULT = "Não informado"


class Animal(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    weight = models.FloatField()
    sex = models.CharField(max_length=20, choices=SexAnimal.choices, default=SexAnimal.DEFAULT)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __repr__(self) -> str:
        return f"<Animal {self.id} - {self.name}>"

