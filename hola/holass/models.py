'''
SENA CBA CENTRO DE BIOTECNOLOGIA AGROPECUARIA
PROGRAMACION DE SOFTWARE

FICHA: 2877795
AUTOR: NICOLAS ANDRES ACOSTA HIGUERA
PROYECTO: HOLA_MUNDO DJANGO (holas/model.py)
FECHA: 02-09-2024
VERSION: 3.0
'''

# Importaciones externas de Django.
from django.db import models

# Create your models here.

class Post(models.Model):
    """
    Esta clase define el modelo de un post.
    
    Args:
        models (Model): Clase que define un modelo de Django.
    
    Returns:
        str: El mensaje del post.
    """
    
    
    message = models.TextField() # Variable que contiene el campo de texto para el mensaje.
    
    def __str__(self):
        '''
        cuando llamamos a un objeto de la clase Post, se devolverá el mensaje del post.
        '''
        return self.message[:50] # Retorna el mensaje del post.

