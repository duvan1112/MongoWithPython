from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from Persons.models import Persons


# Create your views here.

@csrf_exempt
def person_api(request):
    if request.method == 'GET':
        persons = Persons.objects.all()
        return JsonResponse(persons.data, safe=False)
    elif request.method == 'POST':
        person_data = JSONParser().parse(request)
        if person_data.is_valid():
            person_data.save()
            return JsonResponse("Persona agregada exitosamente", safe=False)
        return JsonResponse("No fue posible agregar la persona")
    '''elif request.method == 'PUT':
        person_data = JSONParser().parse(request)
        person = Persons.objects.get(_id=['_id'])
        persons_serializer = PersonsSerializer(person, data=person_data)
        if persons_serializer.is_valid():
            persons_serializer.save()
            return JsonResponse("Datos de persona actualizados", safe=False)
        return JsonResponse("No fue posible actualizar los datos de la persona")
    elif request.method == 'DELETE':
        person = Persons.objects.get(_id=id)
        person.delete()
        return JsonResponse("Persona eliminada")'''
