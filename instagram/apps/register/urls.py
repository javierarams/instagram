from django.urls import path, include
from apps.register.views import index, register_view, profile_view, logout_view, follow_view, follow_user, friends_profile, edit_profile, change_password
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
    path('change-password/', change_password, name='change_password')
]
