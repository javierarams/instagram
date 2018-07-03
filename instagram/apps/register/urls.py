from django.urls import path, include
from apps.register.views import (index, 
                                register_view, 
                                profile_view, 
                                logout_view, 
                                follow_view, 
                                follow_user, 
                                friends_profile, 
                                edit_profile, 
                                change_password,
                                list_followers,
                                list_followings,
                                list_follow_requests,
                                accept_follow_request)
from django.contrib.auth import views as auth_views, logout

app_name = 'register'

urlpatterns = [ 
	path('', index, name='index'),
	path('new', register_view, name='register'),
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='register/login_form.html',
            redirect_authenticated_user=True
        ),
        name='login',
    ),
    path('profile/', profile_view, name='profile'),
    path('profile/<username>/', friends_profile, name='friends_profile'),
    path('logout/', logout_view, name='logout'),
    path('follow/', follow_view, name='follow'),
    path('follow_user/', follow_user, name='follow_user'),
    path('edition/', edit_profile, name='edition'),
    path('password/', change_password, name='change_password'),
    path('followers/', list_followers, name='followers'),
    path('following/', list_followings, name='following'),
    path('follow_requests/', list_follow_requests, name='follow_requests'),
    path('accept_request/', accept_follow_request, name='accept_request'),
]
