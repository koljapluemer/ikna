from .models import Word
import uuid
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.core.paginator import Paginator

def ensure_user(request):
    if not request.user.is_authenticated:
        username = "lazy_" + uuid.uuid4().hex[:10]
        user = User.objects.create_user(username=username)
        user.set_unusable_password()
        user.save()
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')

def vocab_add(request, pk=None):
    ensure_user(request)
    # If pk is provided, fetch the word; otherwise, None
    word = get_object_or_404(Word, pk=pk, user=request.user) if pk else None

    if request.method == "POST":
        native = request.POST.get('native', '')
        translation = request.POST.get('translation', '')
        script = request.POST.get('script', '')
        native_info = request.POST.get('native_info', '')
        translation_info = request.POST.get('translation_info', '')

        if word:
            word.native = native
            word.translation = translation
            word.script = script
            word.native_info = native_info
            word.translation_info = translation_info
            word.save()
            return redirect('vocab_list')
        else:
            word = Word.objects.create(
                user=request.user,
                native=native,
                translation=translation,
                script=script,
                native_info=native_info,
                translation_info=translation_info
            )
            return redirect('vocab_add')
    return render(request, 'vocab/add.html', {'word': word})


def vocab_list(request):
    ensure_user(request)
    words = Word.objects.filter(user=request.user).order_by('-id')
    paginator = Paginator(words, 50) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'vocab/list.html', {'page_obj': page_obj})