from django.urls import path
from .views import *

urlpatterns = [
    path('', vocab_list, name='vocab_list'),
    path('add/', vocab_add, name='vocab_add'),
    path('<int:pk>/edit/', vocab_add, name='vocab_edit'),
    path('list/', vocab_list, name='vocab_list'),
    path('practice/', vocab_practice, name='vocab_practice'),
    path('prompt/', prompt, name='prompt'),
]
