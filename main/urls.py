from django.urls import path
from .views import add_word

urlpatterns = [
    path('add/', add_word, name='add_word'),
]
