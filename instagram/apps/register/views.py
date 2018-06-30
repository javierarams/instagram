from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from apps.register.forms import RegisterForm, UserForm


def index(request):
    return render(request, 'register/login_form.html')


def register_view(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid() and user_form.is_valid():
            user = User.objects.create_user(**user_form.cleaned_data)
            login(request, user)
            form = form.save(commit=False)
            form.user = user
            form.save()
            return redirect('register:profile')
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

def friends_profile(request, userid):
    print(userid)
    user = User.objects.get(id=userid)
    return render(request, 'register/profile.html', {'user': user})

def logout_view(request):
    logout(request)
    return render(request, 'register/logout.html')

def follow_view(request):
    users = User.objects.all()
    return render(request, 'register/follow.html', {'users': users})

#def find_friend(request):
    #if request.user.is_authenticated:
        #if User.objects.get(username=username).exists():
    #friend = User.objects.get(username=username)



def follow_user(request):
    #user2 = User(request.POST)
    user = request.user
    print(request.POST.getlist('followBtn'))
    userid = request.POST.getlist('followBtn')[0]
    user2 = User.objects.get(id=userid)
    print(user2.username)
    user2.userprofile.follows.add(user.userprofile) # user follows user2
    following = user.userprofile.follows.all()
    followers = user.userprofile.followed_by.all()
    print("llega")
    users = User.objects.all()
    for usuarios in following: #NO IMPRIME NADA
        print(usuarios.username)
    return render(request, 'register/follow.html', {'users': users})
#user.userprofile.follows.all() # list of userprofiles of users that tim follows
#user.userprofile.followed_by.all() # list of userprofiles of users that follow chris


