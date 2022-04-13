import json

def valid_graph(vertices,edges,is_directed,is_valorado,name):

	if(is_valorado):
		file_name = direcionados_com_peso(vertices, edges, name)	
	else:
		file_name = direcionados_sem_peso(vertices, edges, name)
	return file_name
		
	

def direcionados_com_peso(vertices, edges, name):
	vert = {'vertices':list(map(str.strip, vertices.split(',')))}
	arest = edges.split(',')

	edge_list = []
	for edge in arest:
		aux_list = []
		try:
			origem, destino_peso = edge.split('->')
			destino,peso = destino_peso.split()
			aux_list.append(origem.strip())
			aux_list.append(destino.strip())
			aux_list.append(int(peso))

			edge_list.append(aux_list)
		except  :
			return("Peso não foi inserido de forma correta ")		
	edg = {'edges': edge_list}

	graph_dict = {}
	graph_dict.update(vert)
	graph_dict.update(edg)
	file_name = name.strip()+'.json'
	print(file_name)
	with open(file_name, 'w') as fp:
		json.dump(graph_dict, fp)
	return(file_name)



def direcionados_sem_peso(vertices, edges, name):
	vert = {'vertices': vertices.split(',')}
	for v in vert:
		v.strip()
	arest = edges.split(',')

	edge_list = []
	for edge in arest:
		try:
			aux_list = []
			origem, destino = edge.split('->')
			aux_list.append(origem)
			aux_list.append(destino)
			edge_list.append(aux_list)
		except :
			return("Erro na inserção ods dados, você queria um grafo valorado ? ")		

	edg = {'edges': edge_list}

	graph_dict = {}
	graph_dict.update(vert)
	graph_dict.update(edg)

	file_name = name.strip()+'.json'

	with open(file_name, 'w') as fp:
		json.dump(graph_dict, fp)
	return(file_name)
