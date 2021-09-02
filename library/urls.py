from django.contrib import admin
from django.urls import path, include
from api.views import *

from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'books', BooksViewSet)
router.register(r'reading', ReadingListViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
