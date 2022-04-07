from django.urls import path
from . import views

urlpatterns = [
    path('', views.plot_graph, name='plot_graph'),
    path('graph/new/', views.graph_new, name='graph_new'),
]