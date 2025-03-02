from django.shortcuts import redirect
from main.models import WordPractice, Word
from main.views.interactions.sr import interaction_sr
from main.views.interactions.thanks_will_remember import interaction_thanks_will_remember
from main.views.utils import ensure_user
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
        return redirect('interaction.thanks_will_remember', pk=word.pk)
    else:
        return redirect('interaction.sr', pk=word.pk)
    
