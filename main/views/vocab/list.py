from django.shortcuts import render
from main.models import Word
from main.views.utils import ensure_user
from django.core.paginator import Paginator

def vocab_list(request):
    ensure_user(request)
    words = Word.objects.filter(user=request.user).order_by('-id')
    paginator = Paginator(words, 50) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'vocab/list.html', {'page_obj': page_obj})
