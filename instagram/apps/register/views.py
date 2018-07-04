from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm
from django.views.decorators.csrf import csrf_exempt

from apps.register.forms import RegisterForm, UserForm, EditUserForm
from apps.register.models import UserProfile


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

def edit_profile(request):
    if request.method == "POST":
        user_form = EditUserForm(request.POST, instance=request.user)
        form = RegisterForm(request.POST, instance=request.user.userprofile)
        if form.is_valid() and user_form.is_valid():
            form.save()
            user_form.save()
            update_session_auth_hash(request, request.user)
            return redirect('register:profile')
    else:
        user_form = EditUserForm(instance=request.user)
        form = RegisterForm(instance=request.user.userprofile)
        args = {'user_form': user_form, 'form':form}
        return render(request, 'register/edit_profile.html', args)

def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('register:profile')

    else:
        form = PasswordChangeForm(user=request.user)
    args = {'form': form}
    return render(request, 'register/change_password.html', args)

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
    return render(request, 'register/profile.html', {'user': user, 'same_user': True})

def friends_profile(request, username):
    user = User.objects.get(username=username)
    same_user = str(user.username) is str(user.username)
    followed = request.user.userprofile.follows.filter(user=user).exists()
    follow_requested = request.user.userprofile.follow_requests.filter(user=user).exists()
    return render(request, 'register/profile.html', {'user': user, 'followed': followed, 'follow_requested': follow_requested, 'same_user': same_user})

def logout_view(request):
    logout(request)
    return render(request, 'register/logout.html')

def follow_view(request):
    users = User.objects.exclude(id=request.user.id)
    return render(request, 'register/follow.html', {'users': users})

@csrf_exempt
def follow_user(request):
    # User logged in
    user = request.user
    # Profile from user we want to follow
    user_to_follow = UserProfile.objects.get(user_id=request.POST.get('user_id'))
    if(user_to_follow.private):
        user = UserProfile.objects.get(user_id=user.id)
        user_to_follow.follow_requests.add(user)
        return HttpResponse('Request sent')
    else:
        user.userprofile.follows.add(user_to_follow)
        return HttpResponse('Following')

def accept_follow_request(request):
    user = request.user
    user_to_accept = UserProfile.objects.get(user_id=request.POST.get('user_id'))
    user.userprofile.followed_by.add(user_to_accept)
    user.userprofile.follow_requests.remove(user_to_accept)
    return HttpResponse('Request accepted')

def list_followers(request):
    user = request.user
    followers = user.userprofile.followed_by.all()
    return render(request, 'register/followers.html', {'followers': followers})

def list_followings(request):
    user = request.user
    followings = user.userprofile.follows.all()
    return render(request, 'register/following.html', {'followings': followings})

def list_follow_requests(request):
    user = request.user
    follow_requests = user.userprofile.follow_requests.all()
    return render(request, 'register/follow_requests.html', {'follow_requests': follow_requests})