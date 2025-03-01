# all the user's prompts
from django.shortcuts import render
from main.models import Prompt

def prompt_list(request):
    request.session["learning_mode"] = "prompts"

    prompts = Prompt.objects.filter(user=request.user).order_by('-id')
    return render(request, 'prompts/list.html', {'prompts': prompts})
