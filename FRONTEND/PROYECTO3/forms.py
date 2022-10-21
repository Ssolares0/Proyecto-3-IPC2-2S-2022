from django import forms

class FileForm(forms.Form):
    file = forms.FileField(label="file")

class FileForm2(forms.Form):
    file2 = forms.FileField(label="file2")

class FileFormSignUp(forms.Form):
	nombres = forms.CharField(label="nombres")
	apellidos= forms.CharField(label= "apellidos")
	username= forms.CharField(label="username")
	correo= forms.CharField(label="correo")
	contraseña=forms.CharField(label="contraseña")

	