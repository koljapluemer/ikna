from .models import Word, WordPractice
import uuid
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.urls import reverse
from django.utils import timezone
from fsrs import Scheduler, Card, Rating, State

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


def vocab_practice(request):
    ensure_user(request)
    # Retrieve all words for the current user.
    words_qs = Word.objects.filter(user=request.user)
    now = timezone.now()
    due_words = []
    
    # For each word, if no practice record exists or it’s due, consider it due.
    for word in words_qs:
        try:
            practice = word.vocab_practices.get(user=request.user)
        except WordPractice.DoesNotExist:
            practice = None
        if practice is None or (practice.due is not None and practice.due <= now):
            due_words.append((word, practice))
    
    # If no words are due, redirect to the word list.
    if not due_words:
        return redirect('vocab_list')
    
    # Select the first due word.
    word, practice = due_words[0]
    
    if request.method == 'POST':
        try:
            answer = int(request.POST.get('answer'))
        except (ValueError, TypeError):
            error_msg = "Invalid answer submitted."
            return render(request, 'vocab/practice.html', {'word': word, 'error': error_msg})
        
        scheduler = Scheduler()
        if practice is None:
            # Create a new card with FSRS defaults.
            card = Card()
        else:
            # Recreate the card from stored practice state.
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
        else:
            error_msg = "Invalid rating value."
            return render(request, 'vocab/practice.html', {'word': word, 'error': error_msg})
        
        # Update the card using the FSRS scheduler.
        card, review_log = scheduler.review_card(card, rating)
        
        # Save the updated card state to the practice record.
        if practice is None:
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
        else:
            practice.card_id = card.card_id
            practice.state = card.state.name if card.state else "Learning"
            practice.step = card.step
            practice.stability = card.stability
            practice.difficulty = card.difficulty
            practice.due = card.due
            practice.last_review = card.last_review
            practice.save()
        
        # Redirect to get the next due word.
        return redirect(reverse('vocab_practice'))
    
    return render(request, 'vocab/practice.html', {'word': word})


def prompt(request):
    return render(request, 'prompts/prompt.html')