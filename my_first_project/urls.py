
from django.contrib import admin
from django.urls import path, include
from my_first_app.views import myView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('car-list/', myView),
]
    

