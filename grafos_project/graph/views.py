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


def graph_new(request):

	if request.method == "POST":

		graph_form = GraphInputForm(request.POST)
		if graph_form.is_valid():
			vertices_input = graph_form.cleaned_data['vertices_input']
			edges_input = graph_form.cleaned_data['edges_input']
			is_directed = graph_form.cleaned_data['is_directed']
			is_valorado = graph_form.cleaned_data['is_valorado']
			name_input = graph_form.cleaned_data['name_input']
			#TODO = VERFICAR SE GRAFO É VALIDO
			if(valid_graph()):
				if(is_directed & is_valorado):
					dicti = direcionados_com_peso(vertices_input, edges_input,name_input)
				else:
					direcionados_sem_peso(vertices_input, edges_input,name_input)

				
				#return redirect('plot_graph')
				return render(request=request, template_name="graph/display_graph.html", context={'graph_form':graph_form, 'dicti':dicti})
		else:
			print("Deu ruim")
			mensagem_erro = "Erro na inserção de valores"
			return render(request=request, template_name="graph/error.html", context={'mensagem_erro':mensagem_erro})
	else:

		graph_form = GraphInputForm()
	return render(request, 'graph/graph_edit.html', {'graph_form' : graph_form})

def direcionados_com_peso(vertices, edges, name):
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
	return(graph_dict)



def direcionados_sem_peso(vertices, edges, name):
	vert = {'vertices': vertices.split(',')}
	arest = edges.split(',')

	edge_list = []
	for edge in arest:
		aux_list = []
		origem, destino = edge.split('->')
		aux_list.append(origem)
		aux_list.append(destino)
		edge_list.append(aux_list)
		
	edg = {'edges': edge_list}

	graph_dict = {}
	graph_dict.update(vert)
	graph_dict.update(edg)

	with open(name+'.json', 'w') as fp:
		json.dump(graph_dict, fp)
	calculate(name+'.json')
	#return(graph_dict)

def valid_graph():
	return True