from django.shortcuts import render
from django.http import HttpResponse
from . import tasks
from .models import Application
from rest_framework import generics
from .serializers import AppSerializer
# Create your views here.


def home(request):
    # task
    # Application.objects.get_or_create(
    #     title="Test",
    #     publisher="Poloes",
    #     publishedYear=1232,
    #     email='mail@mail.cim',
    # )
    tasks.save_product_by_id.delay()
    return HttpResponse("<h1>Loading..</h1>")


class ApplicationApiView(generics.ListAPIView):
    queryset = Application.objects.all()

    # Application.objects.get_or_create(
    #     title=123,
    #     publisher=123,
    #     publishedYear=234,
    #     email=777,
    # )
    serializer_class = AppSerializer