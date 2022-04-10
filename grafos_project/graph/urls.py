from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.graph_new, name='graph_new'),
    path('graph/<str:file_name>', views.plot_graph, name='plot_graph'),
]

