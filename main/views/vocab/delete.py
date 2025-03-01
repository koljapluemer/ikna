from django.shortcuts import get_object_or_404, redirect
from main.models import Word
from main.views.utils import ensure_user
from django.contrib import messages

def vocab_delete(request, pk=None):
    ensure_user(request)
    word = get_object_or_404(Word, pk=pk, user=request.user) 
    word.delete()
    messages.success(request, 'Word deleted')

    return redirect('vocab.list')
