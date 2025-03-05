from django.shortcuts import redirect, render
from main.models import WordPractice, Word
from main.views.utils import create_new_practice_obs, ensure_user, handle_sr_answer
import random
from django.utils import timezone
from django.contrib import messages

def vocab_practice(request):
    ensure_user(request)
    request.session["learning_mode"] = "vocab"

    words_qs = Word.objects.filter(user=request.user)
    now = timezone.now()
    due_words = []

    # For each word, if no practice record exists or it’s due, consider it due.
    for word in words_qs:
        practice = word.vocab_practices.filter(user=request.user).first() # type: ignore
        if word.script != None and (practice is None or (practice.due is not None and practice.due <= now)):
            due_words.append((word, practice))
    
    if not due_words:
        messages.warning(request, "Nothing to practice right now.")
        return redirect('vocab.list')
    
    word, practice = random.choice(due_words)

    # use different interactions according to
    # whether word is seen for the first time
    if practice is None:
        create_new_practice_obs(word, request.user)
        return render(request, 'vocab/learn.html', {'word': word})
    else:
        answer = request.POST.get("answer", -99)
        handle_sr_answer(answer, practice)
        return redirect('interaction.sr', pk=word.pk)
    
