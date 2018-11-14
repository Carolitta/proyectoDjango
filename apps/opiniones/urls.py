from django.urls import path
from . import views

urlpatterns = [
    path('',views.inicio,name='inicio'),
    path('comenzar/',views.comenzar,name='comenzar'),
    path('opinion/<pk>',views.detalles,name='detalles'),
<<<<<<< HEAD
    path('opiniones/',views.listaOpiniones,name='listar'),
    path('opiniones/<pk>/modificar/', views.modificar, name='editar'),
=======
    #path('post/nuevo/',views.nuevoPost,name = 'nuevo'),
    #path('post/<pk>/modificar/', views.modificar, name='modificar'),
>>>>>>> 2ccfec220ca0e732a3ff0d01e5bc70886888becc
]