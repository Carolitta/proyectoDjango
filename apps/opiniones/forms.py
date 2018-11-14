from django import forms
from .models import Opinion


class FormularioOpinion(forms.ModelForm):
	class Meta:
		model = Opinion
		fields = ('calif_claridad','calif_material','calif_general','comentario','curso','becario')
		widgets={
			'comentario': forms.TextInput(attrs={'class':'form-control'}),
			'becario': forms.Select(attrs = {'class':'custom-select'}),
					}