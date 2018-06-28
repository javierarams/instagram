from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.register.forms import RegisterForm, UserForm


def index(request):
    return render(request, 'register/index.html')


def register_view(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid() and user_form.is_valid():
            user = user_form.save()
            form = form.save(commit=False)
            form.user = user
            form.save()
            return redirect('register:index')
    else:
        user_form = UserForm()
        form = RegisterForm()
    return render(request, 'register/register_form.html', {'user_form': user_form, 'form':form})
