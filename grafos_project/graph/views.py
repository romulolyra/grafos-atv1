from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect

from .models import Vertex, Edge
from .forms import *

def plot_graph(request):
	vertices = Vertex.objects.all()
	return render(request,'graph/display_graph.html',{'vertices' : vertices})

def graph_new(request):

	if request.method == "POST":

		graph_form = GraphInputForm(request.POST)
		if graph_form.is_valid():
			vertices_input = graph_form.cleaned_data['vertices_input']
			edges_input = graph_form.cleaned_data['edges_input']
			is_directed = graph_form.cleaned_data['is_directed']
			name_input = graph_form.cleaned_data['name_input']
			get_input_vertices(vertices_input, edges_input)
			return redirect('plot_graph')
		else:
			print("Deu ruim")
	else:

		graph_form = GraphInputForm()
	return render(request, 'graph/graph_edit.html', {'graph_form' : graph_form})


def get_input_vertices(vertices, edges):
	vert = {'vertices': vertices.split(',')}
	arest = edges.split(',')

	edge_list = []
	for edge in arest:
		aux_list = []
		origem, destino_peso = edge.split('->')
		destino,peso = destino_peso.split()
		aux_list.append(origem)
		aux_list.append(destino)
		aux_list.append(int(peso))

		edge_list.append(aux_list)
		
	edg = {'edges': edge_list}

	print(vert)
	print(edg)