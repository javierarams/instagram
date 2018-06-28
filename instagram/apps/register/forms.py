from django import forms

from apps.register.models import User

GENDERS = (
    		('M', 'M'),
    		('F', 'F'),
   			('X', 'X'),
		)

class RegisterForm(forms.ModelForm):

	class Meta:
		model = User

		fields = [
			'nickname',
			'name',
			'website',
			'bio',
			'phone',
			'email',
			'gender',
			'private',
			'sugest',
		]
		labels = {
			'nickname': 'Nickname',
			'name': 'Name',
			'website': 'Website',
			'bio': 'Bio',
			'phone': 'Phone',
			'email': 'Email',
			'gender': 'Gender',
			'private': 'Private',
			'sugest': 'Sugest',
		}

		widgets = {
			'nickname': forms.TextInput(attrs={'class': 'form-control'}),
			'name': forms.TextInput(attrs={'class': 'form-control'}),
			'website': forms.TextInput(attrs={'class': 'form-control'}),
			'bio': forms.TextInput(attrs={'class': 'form-control'}),
			'phone': forms.TextInput(attrs={'class': 'form-control'}),
			'email': forms.EmailInput(attrs={'class': 'form-control'}),
			'gender': forms.RadioSelect(choices=GENDERS, attrs={'class': 'form-control'}),
			#'private': forms.
			#'sugest': forms.BooleanField(),
			#'gender': forms.ChoiceField(choices=GENDERS, attrs={'class': 'form-control'}),
			#'private': forms.BooleanField(required=False, attrs={'class': 'form-control'}),
			#'sugest': forms.BooleanField(required=False, attrs={'class': 'form-control'}),
		}

		

		