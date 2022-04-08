from django.urls import path
from . import views

urlpatterns = [
    path('', views.graph_new, name='graph_new'),
    path('graph/new', views.plot_graph, name='plot_graph'),
]