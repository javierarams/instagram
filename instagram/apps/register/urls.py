from django.urls import path, include
from apps.register.views import index, register_view, profile_view, logout_view, follow_view, follow_user
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
    path('logout/', logout_view, name='logout'),
    path('follow/', follow_view, name='follow'),
    path('follow_user/', follow_user, name='follow_user'),
]
