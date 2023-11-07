from django.urls import path
from tdaa.views import home, sobre


urlpatterns = [
    path('home/', home),
    path('sobre/', sobre ),
]