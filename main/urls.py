from django.urls import path
from .views import *

urlpatterns = [
    path('add/', vocab_add, name='vocab_add'),
    path('<int:pk>/edit/', vocab_add, name='vocab_edit'),
    path('list/', vocab_list, name='vocab_list'),
]
