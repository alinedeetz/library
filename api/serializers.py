from rest_framework import routers, serializers, viewsets
from .models import *

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ('__all__')

class ReadingListSerializer(serializers.ModelSerializer):
    model = ReadingList
    fields = ('__all__')

class MoviesSerializer(serializers.ModelSerializer):
    model = Movies
    fields = ('__all__')