from django.shortcuts import render
from .models import data
from .serialzers import Serailizerdata
# Create your views here.
from rest_framework import viewsets , mixins


class easyviewset(viewsets.ModelViewSet):
    serializer_class = Serailizerdata
    queryset = data.objects.all()


