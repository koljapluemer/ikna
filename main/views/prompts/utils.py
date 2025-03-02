
from django.shortcuts import get_object_or_404, redirect
from main.models import Prompt
from django.contrib import messages


def activate_prompt(request, pk):
    prompt = Prompt.objects.get(pk=pk)
    prompt.is_active_prompt = True
    prompt.save()
    # deactivate all other prompts
    prompts = Prompt.objects.filter(user=request.user, is_active_prompt=True).exclude(pk=pk)
    for p in prompts:   
        p.is_active_prompt = False
        p.save()
    # TODO: smarter redirect here
    return redirect('prompt.list')

def deactivate_prompt(request, pk):
    prompt = Prompt.objects.get(pk=pk)
    prompt.is_active_prompt = False
    prompt.save()
    return redirect('prompt.list')


def get_prompt(request, pk=None):
    if pk:
        prompt = get_object_or_404(Prompt, pk=pk, user=request.user)
    else:
        prompt = Prompt.objects.filter(user=request.user, is_active_prompt=True).first()
        if not prompt:
            messages.warning(request, "There is no active prompt.")
            return redirect('prompt.new')
    return prompt