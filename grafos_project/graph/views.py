from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect

import json
from .models import Vertex, Edge
from .forms import *
from .main import calculate


def plot_graph(request):
	vertices = Vertex.objects.all()
	return render(request,'graph/display_graph.html',{'vertices' : vertices})

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'graph_edit.html', {'form': form})
def graph_new(request):

	if request.method == "POST":

		graph_form = GraphInputForm(request.POST)
		if graph_form.is_valid():
			vertices_input = graph_form.cleaned_data['vertices_input']
			edges_input = graph_form.cleaned_data['edges_input']
			is_directed = graph_form.cleaned_data['is_directed']
			name_input = graph_form.cleaned_data['name_input']

			get_input_vertices(vertices_input, edges_input,name_input)
			return redirect('plot_graph')
		else:
			print("Deu ruim")
	else:

		graph_form = GraphInputForm()
	return render(request, 'graph/graph_edit.html', {'graph_form' : graph_form})

#TO DO : Bug ao receber grafo não direcionado
def get_input_vertices(vertices, edges, name):
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

	graph_dict = {}
	graph_dict.update(vert)
	graph_dict.update(edg)

	with open(name+'.json', 'w') as fp:
		json.dump(graph_dict, fp)
	calculate(name+'.json')

def handle_uploaded_file(f):
    with open('name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)