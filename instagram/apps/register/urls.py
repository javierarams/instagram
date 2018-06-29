from django.urls import path, include
from apps.register.views import index, register_view, profile_view
from django.contrib.auth import views as auth_views

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
]
