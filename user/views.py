from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import RegistrationForm, ProfileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        #profile_form = ProfileForm(request.POST)

        if form.is_valid(): #and profile_form.is_valid()
            user = form.save()
            # profile = profile_form.save(commit=False)
            # profile.user = user
            # profile.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            print('======user registered============')
        
            return redirect('login')
    else:
        form = RegistrationForm()
        #profile_form = ProfileForm()
    #context = {'form': form, 'profile_form': profile_form}
    #return render(request, 'register.html', context)
    context = {'form': form}
    return render(request, 'register.html', context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def profile(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST)
        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.save()
        
            return redirect('profile')
    else:
        profile_form = ProfileForm()
    context = {'profile_form': profile_form}
    return render(request, 'profile.html', context)