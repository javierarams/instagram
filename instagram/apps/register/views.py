from django.shortcuts import render, redirect
from django.http import HttpResponse

from apps.register.forms import RegisterForm, UserForm


def index(request):
    return render(request, 'register/index.html')


def register_view(request):
    if request.method == 'POST':
        print(1)
        user_form = UserForm(request.POST)
        print(2)
        form = RegisterForm(request.POST)
        print(3)
        if form.is_valid() and user_form.is_valid():
            print(4)
            user_form.save()
            form = upf.save(commit=False)
            form.user = user
            form.save()
        print(5)
        return redirect('register:index')
    else:
        print('else')
        user_form = UserForm()
        form = RegisterForm()

    return render(request, 'register/register_form.html', {'user_form': user_form, 'form':form})
