from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
from apps.settings.models import Sesstings


def getType(request):
    item = Sesstings.objects.values('id','name','add_time').filter(type=True)
    resulte = []
    for i in item:
        resulte.append(i)

    return JsonResponse(resulte,safe=False)