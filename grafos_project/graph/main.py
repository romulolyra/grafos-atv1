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

## Falta fazer ainda!
##def short_path(init, end, graph):

##SABER SE CONSIDERA node_a OU node_b VIZINHO DELE MESMO OU NAO
def is_adj(node_a, node_b, graph):
	for edge in graph['edges']:
		if (edge[0] == node_a and edge[1] == node_b):
			return True
		elif (edge[0] == node_b and edge[1] == node_a):
			return True
	return False

##SEPARA OS NODES DE ENTRADA E SAIDA, CONISDERANDO O PRIMEIRO NODE DO LINK COMO PONTO DE SAIDA E O SEGUNDO COMO DE CHEGADA
##DEVE SERVIR PARA GRAFOS NAO DIRECIONADOS, SERIA APENAS IGNORAR ESSA SEPARACAO
def list_adj(node_a, graph):
	adjs = {'in': [], 'out': [], 'loop': False}
	for edge in graph['edges']:
		if (edge[0] == node_a and edge[1] == node_a):
			adjs['loop'] = True
		elif (edge[0] == node_a):
			adjs['out'].append(edge[1])
		elif (edge[1] == node_a):
			adjs['in'].append(edge[0])
	return adjs

def calculate(file_name):
	with open(file_name) as file:
		graph = json.load(file)

		num_nodes = count_nodes(graph['vertices'])
		
		num_edges = count_edges(graph['edges'])

		vizinho = is_adj('ser1', 'ser2', graph)

		lista_adj = list_adj('ser2', graph)

		#print("A lista de adjacentes do node ser2 eh: ", lista_adj)
		#print("Os nodes ser1 e ser3 sao vizinhos: ", vizinho)
		print("Numero de Nodes neste grafo eh de: ", num_nodes)
		print("Numero de Arestas neste grafo eh de: ", num_edges)