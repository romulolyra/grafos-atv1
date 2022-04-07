from django import forms
from .models import Vertex, Edge


class VertexForm(forms.ModelForm):
	class Meta:
		model = Vertex
		fields = ("label",)
