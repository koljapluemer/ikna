from django.contrib.auth.models import User
from django.contrib.auth import login
import uuid

def ensure_user(request):
    if not request.user.is_authenticated:
        username = "lazy_" + uuid.uuid4().hex[:10]
        user = User.objects.create_user(username=username)
        user.set_unusable_password()
        user.save()
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
