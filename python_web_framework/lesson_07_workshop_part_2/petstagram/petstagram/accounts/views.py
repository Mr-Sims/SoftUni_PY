from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from petstagram.accounts.forms import LoginForm, ProfileForm
from petstagram.accounts.forms import RegisterForm
from petstagram.accounts.models import Profile
from petstagram.pets.models import Pet


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('landing page')
    else:
        form = LoginForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid:
            user = form.save()
            login(request, user)
            return redirect('landing page')
    else:
        form = RegisterForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


def logout_user(request):
    logout(request)
    return redirect('landing page')


@login_required
def profile_details(request):
    profile = Profile.objects.get(pk=request.user.id)
    if request.method == "POST":
        form = ProfileForm(
            request.POST,
            request.FILES,
            instance=profile,
        )
        if form.is_valid():
            form.save()
            return redirect('profile details')
    else:
        form = ProfileForm(instance=profile)
    user_pets = Pet.objects.filter(user_id = request.user.id)
    context = {
        'form': form,
        'pets': user_pets,
        'profile': profile,
    }
    return render(request, 'accounts/user_profile.html', context)

