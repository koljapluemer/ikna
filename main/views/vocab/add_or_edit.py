from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from main.models import Word
from main.views.utils import ensure_user
from django.contrib import messages

def vocab_add_or_edit(request, pk=None):
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
            return redirect('vocab.list')
        else:
            word = Word.objects.create(
                user=request.user,
                native=native,
                translation=translation,
                script=script,
                native_info=native_info,
                translation_info=translation_info
            )
            messages.success(request, 'Word added successfully')
            return redirect('vocab.add')
    return render(request, 'vocab/add.html', {'word': word})
