from django.http import HttpResponse
from . import models


def getAllCars(request):

    allCars = models.CarModel.objects.all()

    return HttpResponse(allCars)


def insertCar(request):

    if request.method == 'POST':

        return HttpResponse("ok")
    else:
        return HttpResponse("not ok")
