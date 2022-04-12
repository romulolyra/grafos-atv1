from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

import json
from .models import Vertex, Edge
from .forms import *
from .graph_manipulation import valid_graph
from .main import calculate

def more_inputs(request, graph_json):
	#graph_json = graph_json
	#y = json.loads()
	messages = calculate(graph_json)

	if request.method == "POST":

		edges2_form = Two_verticesForm(request.POST)
		if edges2_form.is_valid():
			destiny_vertex = edges2_form.cleaned_data['destiny_vertex']
			origin_vertex = edges2_form.cleaned_data['origin_vertex']
			origin_vertex = edges2_form.cleaned_data['operations']


			
			graph_json = valid_graph(vertices_input,edges_input,is_directed,is_valorado,name_input)
			if('.json' not in graph_json):
				return render(request=request, template_name="graph/error.html", context={'mensagem_erro':graph_json})

			return plot_graph(request,graph_json)


	else:
		form = Two_verticesForm()
		return render(request,'graph/aditional_input.html',context = {'messages' : messages,'form' : form})


def plot_graph(request, graph_json):
	#graph_json = graph_json
	#y = json.loads()
	
	return render(request,'graph/display_graph.html',context = {'graph_json' : graph_json})


def graph_new(request):

	if request.method == "POST":

		graph_form = GraphInputForm(request.POST)
		if graph_form.is_valid():
			vertices_input = graph_form.cleaned_data['vertices_input']
			edges_input = graph_form.cleaned_data['edges_input']
			is_directed = graph_form.cleaned_data['is_directed']
			is_valorado = graph_form.cleaned_data['is_valorado']
			name_input = graph_form.cleaned_data['name_input']

			
			graph_json = valid_graph(vertices_input,edges_input,is_directed,is_valorado,name_input)
			if('.json' not in graph_json):
				return render(request=request, template_name="graph/error.html", context={'mensagem_erro':graph_json})

			return plot_graph(request,graph_json)

		else:
			print("Deu ruim")
			mensagem_erro = "Erro na inserção de valores"
			return render(request=GET, template_name="graph/error.html", context={'mensagem_erro':mensagem_erro})
	else:

		graph_form = GraphInputForm()
	return render(request, 'graph/graph_edit.html', {'graph_form' : graph_form})


def retorna_vertices(arquivo):
    return arquivo['vertices']