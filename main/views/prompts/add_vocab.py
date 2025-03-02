from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from main.models import Prompt, Word
from main.views.prompts.utils import get_prompt



# here, the user can add the vocab that they need in the context of this prompt
# the form in the template tracks only a list of native words, rest is added later
def prompt_add_vocab(request, pk = None):
    prompt = get_prompt(request, pk)
    if request.method == 'POST':
        native_words = request.POST.getlist('native_words')
        for native in native_words:
            if native:  # Ignore empty words
                w = Word.objects.create(user=request.user, native=native)
                w.prompts.add(prompt)
        return redirect('prompt.list')
    return render(request, 'prompts/add_vocab.html', {'prompt': prompt})
