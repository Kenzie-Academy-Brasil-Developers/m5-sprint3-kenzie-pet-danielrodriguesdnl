from django.forms import ValidationError, model_to_dict
from rest_framework.views import APIView, Request, Response, status

from .models import Animal

class AnimalView(APIView):
    def get(self, request: Request):
        animals = Animal.objects.all()

        animals_list = [model_to_dict(animal) for animal in animals]

        return Response(animals_list)

    def post(self, request: Request):
        animal = Animal(**request.data)
        
        try:
            animal.full_clean()
        except ValidationError as err:
            import ipdb
            
            ipdb.set_trace()

            return Response("")
        
        animal.save()


        animal_dict = model_to_dict(animal)

        return Response(animal_dict, status.HTTP_201_CREATED)