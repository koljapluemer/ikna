from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from main.models import Prompt, Word



# here, the user can add the vocab that they need in the context of this prompt
# the form in the template tracks only a list of native words, rest is added later
def prompt_add_vocab(request, pk = None):
    if pk:
        prompt = get_object_or_404(Prompt, pk=pk, user=request.user)
    else:
        prompt = Prompt.objects.filter(user=request.user, is_active_prompt=True).first()
        if not prompt:
            messages.warning(request, "There is no active prompt.")
            return redirect('prompt.new')
    if request.method == 'POST':
        native_words = request.POST.getlist('native_words')
        for native in native_words:
            if native:  # Ignore empty words
                w = Word.objects.create(user=request.user, native=native)
                w.prompts.add(prompt)
        return redirect('prompt.list')
    return render(request, 'prompts/add_vocab.html', {'prompt': prompt})
