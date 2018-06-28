from django.shortcuts import render
from django.http import HttpResponse
from apps.register.forms import RegisterForm
# Create your views here.
def index(request):
    return render(request, 'register/index.html')

def register_view(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
				form.save()
		return redirect('register:index')
	else:
		form = RegisterForm()

	return render(request, 'register/register_form.html', {'form':form})
