from django.urls import path
from tdaa.views import home, sobre, contato, blog


urlpatterns = [
    path('', home),
    path('sobre/', sobre ),
    path('contato/', contato ),
    path('blog/', blog ),
]