from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth import logout,authenticate,login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required



@login_required
def home(request):
    return render(request,'home.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect('/home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')