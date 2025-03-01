from django.shortcuts import redirect


def handle_redirect_after_interaction(learning_mode, learning_context):
    if learning_mode == "vocab":
        return redirect('vocab.practice')
    elif learning_mode == "prompt":
        return redirect('prompt_list')