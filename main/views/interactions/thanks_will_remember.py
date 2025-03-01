from fsrs import Card
from fsrs import Scheduler, Card, Rating, State
from django.shortcuts import render, redirect, get_object_or_404

from main.models import WordPractice, Word
from main.views.interactions.utils import handle_redirect_after_interaction


def interaction_thanks_will_remember(request, pk):
    word = get_object_or_404(Word, pk=pk, user=request.user )
    if request.method == 'POST':
        card = Card()
        WordPractice.objects.create(
                        user=request.user,
                        word=word,
                        card_id = card.card_id,
                        state = card.state.name if card.state else "Learning",
                        step = card.step,
                        stability = card.stability,
                        difficulty = card.difficulty,
                        due = card.due,
                        last_review = card.last_review,
                    )
        return handle_redirect_after_interaction(request)
    elif request.method == 'GET':
        return render(request, 'interactions/thanks_will_remember.html', {'word': word})