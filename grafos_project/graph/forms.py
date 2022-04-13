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
	# Opções de 1 vertice
	operator_vertex = forms.CharField(label='Vertice :', max_length=50, required = False)
	operation_one = forms.CharField(label='Operação1 :', max_length=50, required = False)


	# two vertices operations
	operation_two = forms.CharField(label='Operação2 :', max_length=50, required = False)
	origin_vertex = forms.CharField(label='Vertice 1 :', max_length=50, required = False)
	destiny_vertex = forms.CharField(label='Vertice 2 :', max_length=50, required = False)

