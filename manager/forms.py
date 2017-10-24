from django import forms

class Signup(forms.Form):
	first_name = forms.CharField(label="first name")
	last_name = forms.CharField(label="last name")
	usrname = forms.CharField(label="username")
	psswd = forms.CharField(label="password", widget=forms.PasswordInput)
	email = forms.EmailField(label="email")

class Addtalk(forms.Form):
	description = forms.CharField(label="description")
	name = forms.CharField(label="name")
	email = forms.EmailField(label="email")
	