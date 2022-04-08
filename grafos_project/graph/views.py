from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect

from .models import Vertex, Edge
from .forms import *

def plot_graph(request):
	vertices = Vertex.objects.all()
	return render(request,'graph/display_graph.html',{'vertices' : vertices})

""" def graph_new(request):

	if request.method == "POST":
		vertex_form = VertexForm(request.POST)
		edge_form = EdgeForm(request.POST)
		graph_form = GraphForm(request.POST)
		if form.is_valid():
			vertice = form.save(commit=False)
			vertice.save()
			return redirect('plot_graph', pk=vertice.pk)
	else:
		vertex_form = VertexForm()
		edge_form = EdgeForm()
		graph_form = GraphForm()
	return render(request, 'graph/graph_edit.html', {'vertex_form': vertex_form,
							'edge_form' : edge_form,
							 'graph_form' : graph_form}) """
def graph_new(request):

	if request.method == "POST":

		graph_form = GraphInputForm(request.POST)
		if graph_form.is_valid():
			vertices_input = graph_form.cleaned_data['vertices_input']
			edges_input = graph_form.cleaned_data['edges_input']
			print(vertices_input)
			print(edges_input)
			return redirect('plot_graph')
		else:
			print("Deu ruim")
	else:

		graph_form = GraphInputForm()
	return render(request, 'graph/graph_edit.html', {'graph_form' : graph_form})



