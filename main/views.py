from django.shortcuts import render, redirect, get_object_or_404
from .forms import WordForm
from .models import Word

def add_word(request):
    if request.method == 'POST':
        form = WordForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = WordForm()
    return render(request, 'vocab/add.html', {'form': form})