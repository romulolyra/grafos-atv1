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
	is_directed =forms.BooleanField(label='É direcionado ? :', initial = False, required = False)
	is_valorado =forms.BooleanField(label='É direcionado ? :', initial = False,required = False)
	name_input = forms.CharField(label ='Nome ? :',max_length=300)
	vertices_input = forms.CharField(label='Vertices :', max_length=800)
	edges_input = forms.CharField(label='Arestas :', max_length=2800)



class Two_verticesForm(forms.Form):
	CHOICES = (
	(11, 'Descobrir se os grafos são adjacentes'),
	(12, 'Descobrir o menor caminho'),)
	operation = forms.ChoiceField(choices=CHOICES,label='Qual a operação desejada ? :')
	origin_vertex = forms.CharField(label='Vertice 1 :', max_length=50)
	destiny_vertex = forms.CharField(label='Vertice 2 :', max_length=50)

