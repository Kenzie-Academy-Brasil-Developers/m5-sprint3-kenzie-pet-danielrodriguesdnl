from django.test import TestCase
from animals.models import Animal
from groups.models import Group
from traits.models import Trait


class AnimalTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.animal_1_data = {
            "name": "Thor",
            "age": "2",
            "weight": "13,8",
            "sex": "Macho"
        }

        cls.animal_1 = Animal.objects.create(**cls.animal_1_data)

        group_data_1 = {"name": "Pastor", "scientific_name": "Canis Lupus"}
        group_data_2 = {"name": "Labrador", "scientific_name": "Labrador Retriver"}

        cls.group_1 = Group(**group_data_1)
        cls.group_2 = Group(**group_data_2)

    def test_one_to_one_relationship_with_group(self):
        self.group_1.animal = self.animal_1
        self.group_1.save()
        
        self.group_2.animal = self.animal_1
        self.group_2.save()

    def test_animal_fields(self):
        self.assertEqual(self.animal_1.name, self.animal_1_data["name"])
        self.assertEqual(self.animal_1.age, self.animal_1_data["age"])
        self.assertEqual(self.animal_1.weight, self.animal_1_data["weight"])
        self.assertEqual(self.animal_1.sex, self.animal_1_data["sex"])


    def test_name_max_length(self):
        animal = Animal.objects.get(id=1)
        max_length = animal._meta.get_field('name').max_length
        self.assertEquals(max_length, 50) 