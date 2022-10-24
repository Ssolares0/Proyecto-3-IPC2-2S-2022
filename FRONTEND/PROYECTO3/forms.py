from django import forms

class FileForm(forms.Form):
    file = forms.FileField(label="file")

class FileForm2(forms.Form):
    file2 = forms.FileField(label="file2")

class FileFormSignUp(forms.Form):
	nombres = forms.CharField(label="nombres")
	apellidos= forms.CharField(label= "apellidos")
	username= forms.CharField(label="username")
	correo= forms.EmailField(label="correo")
	contraseña=forms.CharField(widget=forms.PasswordInput())

class FileFormRecursos(forms.Form):
	idRecurso= forms.CharField(label="idRecurso")
	nombre= forms.CharField(label="nombre")
	abreviatura = forms.CharField(label="abreviatura")
	metrica= forms.CharField(label="metrica")
	tipo = forms.CharField(label="tipo")
	valorxhora= forms.CharField(label="valorxhora")

class FileFormCategorias(forms.Form):
	idCategoria= forms.CharField(label="idCategoria")
	nombreCategoria= forms.CharField(label="nombreCategoria")
	descripcionCategoria = forms.CharField(label="descripcionCategoria")
	cargaTrabajo= forms.CharField(label="cargaTrabajo")

	idConfiguracion = forms.CharField(label="idConfiguracion")
	nombreConfiguracion= forms.CharField(label="nombreConfiguracion")
	descripcionConfiguracion= forms.CharField(label="descripcionConfiguracion")

	idRecursosConfiguracion= forms.CharField(label="idRecursosConfiguracion")
	cantidad= forms.CharField(label="cantidad")



	