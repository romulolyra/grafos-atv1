from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

import json

from graph.graph_manipulation import valid_graph

from .models import Vertex, Edge
from .forms import *
from .main import calculate


def plot_graph(request, graph_json):
	#graph_json = graph_json
	#y = json.loads()
	
	return render(request,'graph/display_graph.html',context = {'graph_json' : graph_json})


def graph_new(request):

	if request.method == "POST":

		graph_form = GraphInputForm(request.POST)
		if graph_form.is_valid():
			# Coletar Grafo
			vertices_input = graph_form.cleaned_data['vertices_input']
			edges_input = graph_form.cleaned_data['edges_input']
			is_directed = graph_form.cleaned_data['is_directed']
			is_valorado = graph_form.cleaned_data['is_valorado']
			name_input = graph_form.cleaned_data['name_input']

			# Opções de 1 vertice
			operator_vertex = graph_form.cleaned_data['operator_vertex']
			operation_one = graph_form.cleaned_data['operation_one']
			
			# Opções de 2 vertices 
			origin_vertex = graph_form.cleaned_data['origin_vertex']
			destiny_vertex = graph_form.cleaned_data['destiny_vertex']
			operation_two = graph_form.cleaned_data['operation_two']

			graph_json = valid_graph(vertices_input,edges_input,is_directed,is_valorado,name_input)
			if('.json' not in graph_json):
				return render(request=request, template_name="graph/error.html", context={'mensagem_erro':graph_json})
			calculate(graph_json, is_directed, is_valorado, origin_vertex,destiny_vertex,operator_vertex)
			
			return plot_graph(request,graph_json)

		else:
			print("Deu ruim")
			mensagem_erro = "Erro na inserção de valores"
			return render(request, template_name="graph/error.html", context={'mensagem_erro':mensagem_erro})
	else:

		graph_form = GraphInputForm()
	return render(request, 'graph/graph_edit.html', {'graph_form' : graph_form})


def retorna_vertices(arquivo):
    return arquivo['vertices']
