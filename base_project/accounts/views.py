from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import ProfileCreationForm, LoginForm
from .models import Profile


def register_account(request):
    if request.user.is_authenticated:
        return render(request, 'accounts/sucess_register.html')

    if request.method == 'POST':
        form = ProfileCreationForm(request.POST)
        if form.is_valid():
            profile = form.save()
            user = profile.owner
            login(request, user)

            return render(request, 'accounts/sucess_register.html')

    else:
        form = ProfileCreationForm()

    return render(request, 'accounts/register.html', {'form': form})


def login_account(request):
    """Login user using stored credentials"""

    next_page = request.GET.get('next', '')
    error = ""
    if request.user.is_authenticated:
        return redirect("review")

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                if next_page:
                    return redirect(next_page)
                return redirect('home')

            error = "Credenciais não não válidas"

    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {"page_title": "Login", 'form': form, "error": error})


def logout_account(request):
    """Logout user"""
    logout(request)
    return redirect('home')

@login_required
def review_account(request):
    return render(request, 'accounts/general_subscription.html')
