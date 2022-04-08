from django.db import models

# Create your models here.

class Graph(models.Model):

	is_directed =models.BooleanField(default=False)
	name = models.CharField(max_length=30, unique=True)

	

class Vertex(models.Model):
	label = models.CharField(max_length=30)
	graph = models.ForeignKey(Graph, on_delete=models.CASCADE)

	def __str__(self):
		return self.label	

class Edge(models.Model):
	origin = models.ForeignKey(Vertex, on_delete=models.CASCADE, related_name='orig')
	destiny = models.ForeignKey(Vertex, on_delete=models.CASCADE, related_name='dest')
	weight = models.IntegerField(default=1)
	graph = models.ForeignKey(Graph, on_delete=models.CASCADE)
	

