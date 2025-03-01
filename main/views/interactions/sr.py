from fsrs import Card
from fsrs import Scheduler, Card, Rating, State
from django.shortcuts import render, redirect, get_object_or_404

from main.views.interactions.utils import handle_redirect_after_interaction


def interaction_sr(request, learning_mode, learning_context, word, practice, answer):
    if request.method == 'POST':
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

        practice.card_id = card.card_id
        practice.state = card.state.name if card.state else "Learning"
        practice.step = card.step
        practice.stability = card.stability
        practice.difficulty = card.difficulty
        practice.due = card.due
        practice.last_review = card.last_review
        practice.save()

        print('learning context: ', learning_mode, learning_context)
        return handle_redirect_after_interaction(learning_mode, learning_context)
    elif request.method == 'GET':
        return render(request, 'interactions/sr.html', {'word': word}) 
        