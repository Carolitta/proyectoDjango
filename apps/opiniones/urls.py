from django.urls import path
from . import views

urlpatterns = [
    path('',views.inicio,name='inicio'),
    path('comenzar/',views.comenzar,name='comenzar'),
    path('opinion/<pk>',views.detalles,name='detalles'),
    path('opiniones/',views.listaOpiniones,name='listar'),
    path('opiniones/<pk>/modificar/', views.modificar, name='editar'),
]