
from django.urls import path, include
from django.contrib import admin
from django.http import HttpResponse
from my_first_app.views import *



urlpatterns = [
   path("listado", CarlistView.as_view()), # ass_view retorna el http response 
   path("detalle/<int:id>", my_view)
]



