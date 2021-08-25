from rest_framework import routers, serializers, viewsets
from .models import *

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ('__all__')


