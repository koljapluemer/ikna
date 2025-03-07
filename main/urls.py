from django.urls import path

from main.views.prompts.add_vocab import prompt_add_vocab
from main.views.prompts.list import prompt_list
from main.views.prompts.new import prompt_new
from main.views.prompts.utils import activate_prompt, deactivate_prompt
from main.views.prompts.vocab_list import prompt_vocab_list
from main.views.vocab.add_or_edit import vocab_add_or_edit
from main.views.vocab.delete import vocab_delete
from main.views.vocab.list import vocab_list
from main.views.vocab.practice import vocab_practice

urlpatterns = [
    # TODO: this one is the one I want as start, I think: path('', combined_queue, name='combined_queue'),
    path('', vocab_add_or_edit, name='home'),
    # vocab
    path('vocab/add/', vocab_add_or_edit, name='vocab.add'),
    path('vocab/<int:pk>/edit/', vocab_add_or_edit, name='vocab.edit'),
    path('vocab/list/', vocab_list, name='vocab.list'),
    path('vocab/practice/', vocab_practice, name='vocab.practice'), # type: ignore
    path('vocab/<int:pk>/delete/', vocab_delete, name='vocab.delete'), 
    # prompts
    path('prompt/new/', prompt_new, name='prompt.new'),
    path('prompt/list/', prompt_list, name='prompt.list'),
    path('prompt/<int:pk>/add_vocab/', prompt_add_vocab, name='prompt.add_vocab'),
    path('prompt/add_vocab/', prompt_add_vocab, name='prompt.add_vocab'),
    path('prompt/<int:pk>/activate/', activate_prompt, name='prompt.activate'),
    path('prompt/<int:pk>/deactivate/', deactivate_prompt, name='prompt.deactivate'),
    path('prompt/<int:pk>/vocab_list/', prompt_vocab_list, name='prompt.vocab_list'),
    path('prompt/vocab_list/', prompt_vocab_list, name='prompt.vocab_list'),
]
