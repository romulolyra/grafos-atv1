from django import forms
from .models import Vertex, Edge, Graph


class VertexForm(forms.ModelForm):
	class Meta:
		model = Vertex
		fields = ("label",)
class EdgeForm(forms.ModelForm):
	class Meta:
		model = Edge
		fields = ("origin", "destiny", "weight",)
class GraphForm(forms.ModelForm):
	class Meta:
		model = Graph
		fields = ("is_directed", "name",)
class GraphInputForm(forms.Form):
	vertices_input = forms.CharField(label='Vertices :', max_length=800)
	edges_input = forms.CharField(label='Arestas :', max_length=2800)

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

    