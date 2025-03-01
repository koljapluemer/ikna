# here, the user can add the vocab that they need in the context of this prompt
# the form in the template tracks only a list of native words, rest is added later
from django.shortcuts import get_object_or_404, redirect, render

from main.models import Prompt, Word


def prompt_add_vocab(request):
    if "active_prompt" not in request.session:
        return redirect('prompt.new')
    prompt = Prompt.objects.filter(pk=request.session["active_prompt"], user=request.user).first()
    if not prompt:
        return redirect('prompt.new')
    if request.method == 'POST':
        native_words = request.POST.getlist('native_words')
        for native in native_words:
            if native:  # Ignore empty words
                w = Word.objects.create(user=request.user, native=native)
                w.prompts.add(prompt)
        return redirect('prompt.list')
    return render(request, 'prompts/add_vocab.html', {'prompt': prompt})
