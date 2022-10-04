from app.views import *
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', home),
    path('<str:name>/', info),
    path('admin/', admin.site.urls),
]
