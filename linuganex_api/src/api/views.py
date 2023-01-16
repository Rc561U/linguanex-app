from django.shortcuts import render
from django.http import HttpResponse
from . import tasks
from .models import Application
from rest_framework import generics
from .serializers import AppSerializer
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response


def home(request):
    tasks.main.delay()
    return HttpResponse("<h1>Scrap information. Please wait and check console..</h1>")


class ApplicationApiView(generics.ListAPIView):
    queryset = Application.objects.all()
    serializer_class = AppSerializer
