from django.urls import path, include
#from . import views
from apps.register.views import index, register_view
app_name = 'register'
urlpatterns = [ 
	path('', index, name='index'),
	path('new', register_view, name='register_create'),
]
