# user can write a story/response to the prompt
def prompt_answer(request, pk):
    prompt = get_object_or_404(Prompt, pk=pk, user=request.user)
    if request.method == 'POST':
        answer = request.POST.get('answer')
        if answer:
            prompt.answer = answer
            prompt.is_finished = True
            prompt.save()
            return redirect('prompt_list')
    return render(request, 'prompts/answer.html', {'prompt': prompt})