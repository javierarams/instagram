from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.register.forms import RegisterForm, UserForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'register/login_form.html')


def register_view(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid() and user_form.is_valid():
            user = user_form.save()
            form = form.save(commit=False)
            form.user = user
            form.save()
            return redirect('register:login')
    else:
        user_form = UserForm()
        form = RegisterForm()
    return render(request, 'register/register_form.html', {'user_form': user_form, 'form':form})

def profile_view(request, pk=None):
    if request.user.is_authenticated:
        print("logged")
    else:
        print("not logged")
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    print(user.username)
    return render(request, 'register/profile.html', {'user': user})
