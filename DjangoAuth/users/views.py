from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.contrib.auth.views import LoginView




def home(request):
    return render(request, "users/index.html")


class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True


def logout(request):
    return render(request, "users/logout.html")


@login_required
def profile(request):
    return render(request, 'users/profile.html')