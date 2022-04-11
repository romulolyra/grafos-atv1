import json
import math

#Retorna um contador representando o numero de nodes no grafo.
def count_nodes(graph):
	num_nodes = 0
	for num_nodes in range(len(graph)):
		num_nodes += 1
	return num_nodes

#Retorna um contador representando o numero de arestas no grafo.
def count_edges(graph):
	num_edges = 0
	for num_edges in range(len(graph)):
		num_edges += 1
	return num_edges

#Retorna um booleano significando se os nodes enviados sao adjacentes ou nao.
def is_adj(node_a, node_b, graph):
	for edge in graph['links']:
		if edge[0] == node_a and edge[1] == node_b:
			return True
		elif edge[0] == node_b and edge[1] == node_a:
			return True
	return False

#Retorna uma lista dos nodes adjacentes ao node escolhido, verificando se esta em um dos pontos de um 'link', de uma aresta.
def list_adj_not_direct(node, graph):
	adjs = []
	for edge in graph['links']:
		if edge[0] == node:
			adjs.append(edge[1])
		elif edge[1] == node:
			adjs.append(edge[0])
	return adjs

#Retorna um dicionario contendo duas lista. Uma lista para os nodes adjacentes que estao saindo do node escolhido
# e outra lista para os nodes adjacentes que estao chegando no node escolhido.
def list_adj_direct(node, graph):
	adjs = {'in': [], 'out': []}
	for edge in graph['links']:
		if edge[0] == node:
			adjs['out'].append(edge[1])
		elif edge[1] == node:
			adjs['in'].append(edge[0])
	return adjs

#Retorna um contador representando o grau do node escolhido.
def node_degree_not_direct(node, graph):
	degree = 0
	for edge in graph['links']:
		if edge[0] == node or edge[1] == node:
			degree += 1
	return degree

#Retorna um dicionario contendo dois contadores. Um contador representando o grau para os nodes que estao saindo do node escolhido e outro contador,
# representando o grau para os nodes que estao chegando no node escolhido.
#  - degree['in'] significa que a aresta esta chegando nele
#  - degree['out'] significa que a aresta esta saindo dele
def node_degree_direct(node, graph):
	degree = {'in': 0, 'out': 0}
	for edge in graph['links']:
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

with open('example.json') as file:
	graph = json.load(file)

	node1 = 'ser6'
	node2 = 'ser5'

	num_nodes = count_nodes(graph['nodes'])
	
	num_edges = count_edges(graph['links'])

	vizinho = is_adj(node1, node2, graph)

	lista_adj_dir = list_adj_direct(node1, graph)

	lista_adj_not_dir = list_adj_not_direct(node1, graph)

	degree_dir = node_degree_direct(node1, graph)

	degree_not_dir = node_degree_not_direct(node1, graph)

	pending = is_pending(node1, graph)

	print("O node eh pendente? ", pending)
	print("Grau direcionado :", degree_dir)
	print("Grau nao direcionado", degree_not_dir)
	print("A lista de adjacentes: ", lista_adj_dir)
	print("A lista de adjacentes: ", lista_adj_not_dir)
	print("Os nodes sao vizinhos? ", vizinho)
	print("Numero de Nodes neste grafo: ", num_nodes)
	print("Numero de Arestas neste grafo: ", num_edges)