# all the user's prompts
def prompt_list(request):
    prompts = Prompt.objects.filter(user=request.user).order_by('-id')
    return render(request, 'prompts/list.html', {'prompts': prompts})
