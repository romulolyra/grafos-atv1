import networkx as nx
import matplotlib.pyplot as plt
from texttable import Texttable
import math
import json
from graph.graph_manipulation import valid_graph

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


def generate_undirected(arquivo, is_valorado):
	grafo = nx.Graph()
	e = []
	for edge in arquivo['edges']:
		e.append(tuple(edge))
	if is_valorado:
		grafo.add_weighted_edges_from(e)
	else:
		grafo.add_edges_from(e)
	return grafo

def generate_directed(arquivo, is_valorado):
	grafo = nx.DiGraph()
	e = []
	for edge in arquivo['edges']:
		e.append(tuple(edge))
	if is_valorado:
		grafo.add_weighted_edges_from(e)
	else:
		grafo.add_edges_from(e)
	return grafo



def best_way_between_two_nodes(graph, source, destiny):
	menor_caminho = nx.dijkstra_path(graph, source, destiny)
	distancia = nx.dijkstra_path_length(graph, source, destiny)
	return [menor_caminho, distancia]


def plota_grafo(graph):
	pos = nx.spring_layout(graph)
	pos = nx.circular_layout(graph)
	nx.draw(graph, pos=pos, with_labels=True, font_weight='bold', node_color='pink', arrowsize=20, node_size=1500)
	edge_weight = nx.get_edge_attributes(graph, 'weight')
	nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_weight)
	plt.show()

def calculate(file_name, is_directed, is_valorado, origin_node,destiny_node,single_node):
  
  # Abre o arquivo json e transforma em um dicionário
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
		if is_valorado:
			shortest_path = best_way_between_two_nodes(graph_lib, origin_node, destiny_node)
		if is_directed == True:
			lista_adj = lista_adj_dir
			grau_origin = degree_dir
		else:
			lista_adj = lista_adj_not_dir
			grau_origin = degree_not_dir
		

    # Gera o grafo direcionado ou não direcionado
		if is_directed == True:
			graph_lib = generate_directed(graph)

		else:
			graph_lib = generate_undirected(graph)
		
    # Plota o grafo em uma tela
		plota_grafo(graph_lib)
	
    t = Texttable()
    t.add_rows([
            ['Função', 'Resultado'], 
            ['É pendente?', pending], 
            [f'Adjacência entre {origin_node} e {destiny_node}', vizinho],
            ['Número de nodes', num_nodes],
            ['Número de arestas', num_edges],
	          [f'Menor caminho entre {origin_node} e {destiny_node}', shortest_path[0]],
		        ['Custo do menor caminho entre {origin_node} e {destiny_node}', shortest_path[1]],
		        [f'Lista de adjacentes de {origin_node}', lista_adj],
		        [f'Grau direcionado de {origin_node}', grau_origin]])
	
    print(t.draw())


   
		


# def get_terminal_input():
# 	vertices_list = []
# 	edges_list = []
# 	vertex = ''
# 	edge = ''
	
# 	is_valorado = bool(input("O vertice será valorado ? Se sim, digite True, caso contrário False: "))
# 	is_direcionado = bool(input("\nO vertice será direcionado ? Se sim, digite True, caso contrário False: "))

# 	while(vertex != 'exit'):
# 		vertex = input("Digite o vértice : (para parar, digite exit)")
# 		vertices_list.append(vertex+',')

# 	while(edge != 'exit'):
# 		edge = input("Digite a aresta : (para parar, digite exit)")
# 		edges_list.append(vertex)

# 	name = input("Digite o nome do grafo: ")

# 	valid_graph(vertices_list,edges_list,is_direcionado,is_valorado, name)


# get_terminal_input()
