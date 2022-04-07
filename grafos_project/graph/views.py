from django.shortcuts import render
from django.shortcuts import redirect

from .models import Vertex, Edge
from .forms import VertexForm

def plot_graph(request):
	vertices = Vertex.objects.all()
	return render(request,'graph/display_graph.html',{'vertices' : vertices})

def graph_new(request):

	if request.method == "POST":
		form = VertexForm(request.POST)
		if form.is_valid():
			vertice = form.save(commit=False)
			vertice.save()
			return redirect('plot_graph', pk=vertice.pk)
	else:
		form = VertexForm()
	return render(request, 'graph/graph_edit.html', {'form': form})
