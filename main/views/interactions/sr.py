from fsrs import Card
from fsrs import Scheduler, Card, Rating, State
from django.shortcuts import render, redirect, get_object_or_404

from main.models import Word, WordPractice
from main.views.interactions.utils import handle_redirect_after_interaction


def interaction_sr(request, pk):
    word = get_object_or_404(Word, pk=pk, user=request.user )
    practice = get_object_or_404(WordPractice, word=word, user=request.user)
    if request.method == 'POST':
        answer = int(request.POST.get('answer'))
        print("ANSWER", answer)

        card = Card(
                card_id = practice.card_id,
                state = State[practice.state] if practice.state else State.Learning,
                step = practice.step,
                stability = practice.stability,
                difficulty = practice.difficulty,
                due = practice.due,
                last_review = practice.last_review,
            )
    
                # Map the submitted answer to an FSRS rating.
        if answer == 1:
            rating = Rating.Again
        elif answer == 2:
            rating = Rating.Hard
        elif answer == 3:
            rating = Rating.Good
        elif answer == 4:
            rating = Rating.Easy

        scheduler = Scheduler()
        card, _ = scheduler.review_card(card, rating)

        practice.card_id = card.card_id
        practice.state = card.state.name if card.state else "Learning"
        practice.step = card.step
        practice.stability = card.stability
        practice.difficulty = card.difficulty
        practice.due = card.due
        practice.last_review = card.last_review

        print("LAST REVIEW", practice.last_review)
        print("DUE", practice.due)
        practice.save()

        return handle_redirect_after_interaction(request)
    elif request.method == 'GET':
        return render(request, 'interactions/sr.html', {'word': word}) 
        