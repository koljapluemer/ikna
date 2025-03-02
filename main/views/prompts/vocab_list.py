from django.shortcuts import get_object_or_404, render
from main.models import Word, Prompt
from main.views.prompts.utils import get_prompt
from main.views.utils import ensure_user
from django.core.paginator import Paginator

def prompt_vocab_list(request, pk=None):
    ensure_user(request)
    prompt = get_prompt(request, pk)
    words = Word.objects.filter(user=request.user, prompts=prompt).order_by('-id')
    paginator = Paginator(words, 50) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'prompts/vocab_list.html', {'page_obj': page_obj, 'prompt': prompt})
