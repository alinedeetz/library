from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *

class BooksViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer 
    queryset = Books.objects.all()

class ReadingListViewSet(viewsets.ModelViewSet):
    serializer_class = ReadingListSerializer
    queryset = ReadingList.objects.all()

class MoviesViewSet(viewsets.ModelViewSet):
    serializer_class = MoviesSerializer
    queryset = Movies.objects.all()