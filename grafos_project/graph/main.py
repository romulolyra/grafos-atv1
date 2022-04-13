import networkx as nx
import matplotlib.pyplot as plt
import math
import json

def count_nodes(graph):
    num_nodes = 0
    for num_nodes in range(len(graph)):
        num_nodes += 1
    return num_nodes

def count_edges(graph):
	num_edges = 0

	for num_edges in range(len(graph)):
		num_edges += 1

	return num_edges

#Retorna um booleano significando se os nodes enviados sao adjacentes ou nao.
def is_adj(node_a, node_b, graph):
	for edge in graph['edges']:
		if edge[0] == node_a and edge[1] == node_b:
			return True
		elif edge[0] == node_b and edge[1] == node_a:
			return True
	return False

#Retorna uma lista dos nodes adjacentes ao node escolhido, verificando se esta em um dos pontos de um 'link', de uma aresta.
def list_adj_not_direct(node, graph):
	adjs = []
	for edge in graph['edges']:
		if edge[0] == node:
			adjs.append(edge[1])
		elif edge[1] == node:
			adjs.append(edge[0])
	return adjs

#Retorna um dicionario contendo duas lista. Uma lista para os nodes adjacentes que estao saindo do node escolhido
# e outra lista para os nodes adjacentes que estao chegando no node escolhido.
def list_adj_direct(node, graph):
	adjs = {'in': [], 'out': []}
	for edge in graph['edges']:
		if edge[0] == node:
			adjs['out'].append(edge[1])
		elif edge[1] == node:
			adjs['in'].append(edge[0])
	return adjs

#Retorna um contador representando o grau do node escolhido.
def node_degree_not_direct(node, graph):
	degree = 0
	for edge in graph['edges']:
		if edge[0] == node or edge[1] == node:
			degree += 1
	return degree

#Retorna um dicionario contendo dois contadores. Um contador representando o grau para os nodes que estao saindo do node escolhido e outro contador,
# representando o grau para os nodes que estao chegando no node escolhido.
#  - degree['in'] significa que a aresta esta chegando nele
#  - degree['out'] significa que a aresta esta saindo dele
def node_degree_direct(node, graph):
	degree = {'in': 0, 'out': 0}
	for edge in graph['edges']:
		if edge[1] == node:
			degree['in'] += 1
		elif edge[0] == node:
			degree['out'] += 1
	return degree

def short_path_undirected(graph, initial_node):
	vertices = graph['vertices']
	index_initial = vertices.index(initial_node)
	edges = graph['edges']
	total_vertices = len(vertices)

	path = [math.inf] * total_vertices
	path[index_initial] = 0

	for _ in range(total_vertices - 1):
		for initial, final, weight in edges:
			if (path[vertices.index(initial)] != math.inf) and (path[vertices.index(initial)] + weight < path[vertices.index(final)]):
				path[vertices.index(final)] = path[vertices.index(initial)] + weight
	return path

def is_pending(node, graph):
	pending = True
	degree = node_degree_not_direct(node, graph)
	if degree != 1:
		pending = False
	return pending


def generate_undirected(arquivo):
	graph = nx.Graph()
	e = []
	for edge in arquivo['edges']:
		e.append(tuple(edge))
	print(e)
	graph.add_weighted_edges_from(e)
	return graph


def generate_directed(arquivo):
	graph = nx.DiGraph()
	e = []
	for edge in arquivo['edges']:
		e.append(tuple(edge))
	print(e)
	graph.add_weighted_edges_from(e)
	return graph


def best_way_between_two_nodes(graph, source, destiny):
	print(f'O menor caminho entre {source} e {destiny} é {nx.dijkstra_path(graph, source, destiny)}')
	print(f'Distância total: {nx.dijkstra_path_length(graph, source, destiny)}')


def plota_grafico(graph):
	pos = nx.spring_layout(graph)
	pos = nx.circular_layout(graph)
	nx.draw(graph, pos=pos, with_labels=True, font_weight='bold', node_color='pink', arrowsize=20, node_size=1500)
	edge_weight = nx.get_edge_attributes(graph, 'weight')
	nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_weight)
	plt.show()

def calculate(file_name, is_directed, is_valorado, origin_node,destiny_node,single_node):
	with open(file_name) as file:

		graph = json.load(file)

		num_nodes = count_nodes(graph['vertices'])
		num_edges = count_edges(graph['edges'])

		vizinho = is_adj(origin_node, destiny_node, graph)

		lista_adj_dir = list_adj_direct(origin_node, graph)

		lista_adj_not_dir = list_adj_not_direct(origin_node, graph)

		degree_dir = node_degree_direct(origin_node, graph)

		degree_not_dir = node_degree_not_direct(origin_node, graph)

		pending = is_pending(origin_node, graph)


		if is_directed == True:
			graph_lib = generate_directed(graph)
			print("Grau direcionado :", degree_dir)
		else:
			graph_lib = generate_undirected(graph)
			print("Grau nao direcionado", degree_not_dir)

		plota_grafico(graph_lib)
		if is_valorado:
			#saber o source e destiny que vem do usuario
			best_way_between_two_nodes(graph_lib, origin_node, destiny_node)
		print("O node eh pendente? ", pending)
		print("A lista de adjacentes: ", lista_adj_dir)
		print("A lista de adjacentes: ", lista_adj_not_dir)
		print("Os nodes sao vizinhos? ", vizinho)
		print("Numero de Nodes neste grafo: ", num_nodes)
		print("Numero de Arestas neste grafo: ", num_edges)