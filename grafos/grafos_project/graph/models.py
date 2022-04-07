from django.db import models

# Create your models here.

class Vertex(models.Model):
	label = models.CharField(max_length=30, unique=True)
	is_directed = models.BooleanField()

class Edge(models.Model):
	origin = models.ForeignKey(Vertex, on_delete=models.CASCADE, related_name='orig')
	destiny = models.ForeignKey(Vertex, on_delete=models.CASCADE, related_name='dest')
	weight = models.IntegerField(default=1)
	