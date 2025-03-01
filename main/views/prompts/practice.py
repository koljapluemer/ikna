# this view is responsible to add translations to the words that were added in the previous view
# words that already have complete data should be learned with the standard fsrs method (ALSO IN THIS VIEW)
def prompt_practice(request, pk):
    prompt = get_object_or_404(Prompt, pk=pk, user=request.user)

    return render(request, 'prompts/practice.html')


