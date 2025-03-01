from django.shortcuts import redirect


def handle_redirect_after_interaction(request):
    if request.session["learning_mode"] == "vocab":
        return redirect('vocab.practice')