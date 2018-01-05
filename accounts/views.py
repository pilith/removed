from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.urls import reverse

from accounts.forms import SignUpForm

# Create your views here.

def signup(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('dnd:index')

    else:
        form = SignUpForm()

    return render(request, 'accounts/signup.html', {'form': form})


