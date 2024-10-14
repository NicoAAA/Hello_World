'''
SENA CBA CENTRO DE BIOTECNOLOGIA AGROPECUARIA
PROGRAMACION DE SOFTWARE

FICHA: 2877795
AUTOR: NICOLAS ANDRES ACOSTA HIGUERA
PROYECTO: HOLA_MUNDO DJANGO (holass/views.py)
FECHA: 02-09-2024
VERSION: 3.0
'''


# Importaciones externas de Django.
from django.shortcuts import render
from django.views.generic import DetailView

# Importaciones locales.
from .models import Post

# Create your views here.

class HomePageView(DetailView):
    '''
    Estable las vistas de la página de inicio.
    
    Args:
        DetailView: Clase que se encarga de mostrar los detalles
        de un objeto específico.
    
    Returns:
        Render: Retorna la página de
        inicio con el primer post.
    '''
    
    model = Post # Selecciona el modelo Post.
    template_name = 'base.html' # Selecciona la plantilla base.html.
    context_object_name = 'post' # Selecciona el objeto de contexto post.
    
    
    def get_object(self):
        """
        Obtiene el primer post.
        
        Returns:
            Post: El primer post.
        """
        return Post.objects.first() # Retorna el primer post.