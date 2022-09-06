from django.urls import path
from .views import index, test


urlpatterns = [
    path('ikvict07.github.io/', index),
    path('test/', test)
]
