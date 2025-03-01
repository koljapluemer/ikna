from django.urls import path

from main.views.vocab.add_or_edit import vocab_add_or_edit
from main.views.vocab.delete import vocab_delete
from main.views.vocab.list import vocab_list
from main.views.vocab.practice import vocab_practice

urlpatterns = [
    # TODO: this one is the one I want as start, I think: path('', combined_queue, name='combined_queue'),
    path('', vocab_add_or_edit, name='home'),
    path('vocab/add/', vocab_add_or_edit, name='vocab.add'),
    path('vocab/<int:pk>/edit/', vocab_add_or_edit, name='vocab.edit'),
    path('vocab/list/', vocab_list, name='vocab.list'),
    path('vocab/practice/', vocab_practice, name='vocab.practice'), # type: ignore
    path('vocab/<int:pk>/delete/', vocab_delete, name='vocab.delete'), 
]
