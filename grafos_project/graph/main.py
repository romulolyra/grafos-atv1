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


def calculate(file_name):
	with open(file_name) as file:
		graph = json.load(file)

		num_nodes = count_nodes(graph['vertices'])
		
		num_edges = count_edges(graph['edges'])

		#vizinho = is_adj('ser1', 'ser2', graph)

		#lista_adj = list_adj('ser2', graph)

		#print("A lista de adjacentes do node ser2 eh: ", lista_adj)
		#print("Os nodes ser1 e ser3 sao vizinhos: ", vizinho)
		return("\nNumero de Nodes neste grafo eh de: "+str(num_nodes)+"\nNumero de Arestas neste grafo eh de: "+str(num_edges))
def two_edges(v1, v2, file_name):
	with open(file_name) as file:
		graph = json.load(file)

		vizinho = is_adj(v1, v2, graph)

		#lista_adj = list_adj('ser2', graph)

		print("A lista de adjacentes do node ser2 eh: ", lista_adj)
		print("Os nodes ser1 e ser3 sao vizinhos: ", vizinho)
		return("\nNumero de Nodes neste grafo eh de: "+str(num_nodes)+"\nNumero de Arestas neste grafo eh de: "+str(num_edges))

