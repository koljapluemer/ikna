from django.contrib.auth.models import User
from django.contrib.auth import login
import uuid
from fsrs import Card
from fsrs import Scheduler, Card, Rating, State
from django.shortcuts import render, redirect, get_object_or_404

from main.models import WordPractice

def ensure_user(request):
    if not request.user.is_authenticated:
        username = "lazy_" + uuid.uuid4().hex[:10]
        user = User.objects.create_user(username=username)
        user.set_unusable_password()
        user.save()
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')

def handle_sr_answer(answer, practice):
    print("answer", answer)
    card = Card(
            card_id = practice.card_id,
            state = State[practice.state] if practice.state else State.Learning,
            step = practice.step,
            stability = practice.stability,
            difficulty = practice.difficulty,
            due = practice.due,
            last_review = practice.last_review,
        )

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
    practice.save()


def create_new_practice_obs(word, user):
    card = Card()
    WordPractice.objects.create(
                    user=user,
                    word=word,
                    card_id = card.card_id,
                    state = card.state.name if card.state else "Learning",
                    step = card.step,
                    stability = card.stability,
                    difficulty = card.difficulty,
                    due = card.due,
                    last_review = card.last_review,
                )