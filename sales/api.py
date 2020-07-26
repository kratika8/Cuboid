from django.core import serializers
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Cuboid


@csrf_exempt
def savesCars(request):
    id=request.POST.get('id','')
    type=request.POST.get('type','')
    value=request.POST.get('value','')
    c=Cuboid.objects.get(id=id)
    if type=="length":
       c.Customer_id=value

    if type == "breadth":
        c.Fuel = value

    if type == "height":
        c.VEHICLE_SEGMENT = value


    student.save()
    return JsonResponse({"success":"Updated"})
