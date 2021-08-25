from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *

class BooksViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer 
    queryset = Books.objects.all()



