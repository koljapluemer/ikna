
from django.shortcuts import redirect
from main.models import Prompt


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