'''
SENA CBA CENTRO DE BIOTECNOLOGIA AGROPECUARIA
PROGRAMACION DE SOFTWARE

FICHA: 2877795
AUTOR: NICOLAS ANDRES ACOSTA HIGUERA
PROYECTO: HOLA_MUNDO DJANGO (holass/apps.py)
FECHA: 02-09-2024
VERSION: 3.0
'''


# Importaciones externas de Django.
from django.apps import AppConfig


class HolassConfig(AppConfig):
    '''
    clase que define la configuración de la aplicación.
    
    Args:
        AppConfig: Clase que define la configuración de una aplicación.
        
    Returns:
        str: El nombre de la aplicación.    
    '''
    default_auto_field = 'django.db.models.BigAutoField' # Define el campo automático.
    name = 'holass' # Define el nombre de la aplicación.
