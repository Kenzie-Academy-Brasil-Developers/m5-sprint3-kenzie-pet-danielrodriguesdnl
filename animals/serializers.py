from groups.models import Group
from groups.serializers import GroupSerializer
from traits.serializers import TraitSerializer
from rest_framework import serializers


from .models import SexAnimal, Animal

class AnimalSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    age = serializers.IntegerField()
    weight = serializers.FloatField()
    sex = serializers.ChoiceField(choices=SexAnimal.choices, default=SexAnimal.DEFAULT)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    traits = TraitSerializer(read_only=True, many=True)


class AnimalDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    age = serializers.IntegerField()
    weight = serializers.FloatField()
    sex = serializers.ChoiceField(choices=SexAnimal.choices, default=SexAnimal.DEFAULT)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    time_between = serializers.SerializerMethodField()

    def get_time_between(self, obj: Animal) -> str:
        return str(obj.updated_at - obj.created_at)


    traits = TraitSerializer(read_only=True, many=True) 
    groups = GroupSerializer()

    def create(self, validated_data: dict) -> Animal:
        group_data = validated_data.pop("groups")

        animal_obj = Animal.objects.create(**validated_data)
        Group.objects.create(**group_data, animal=animal_obj)

        return animal_obj

    def update(self, instance: Animal, validated_data: dict) -> Animal:
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()
        
        return instance