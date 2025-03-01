# here, the user can add the vocab that they need in the context of this prompt
# the form in the template tracks only a list of native words, rest is added later
def prompt_add_vocab(request, pk):
    prompt = get_object_or_404(Prompt, pk=pk, user=request.user)
    if request.method == 'POST':
        native_words = request.POST.getlist('native_words')
        for native in native_words:
            Word.objects.create(user=request.user, native=native, prompts=[prompt])
        return redirect('prompt_list')
    return render(request, 'prompts/add_vocab.html', {'prompt': prompt})

