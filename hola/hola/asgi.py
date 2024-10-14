'''
SENA CBA CENTRO DE BIOTECNOLOGIA AGROPECUARIA
PROGRAMACION DE SOFTWARE

FICHA: 2877795
AUTOR: NICOLAS ANDRES ACOSTA HIGUERA
PROYECTO: HOLA_MUNDO DJANGO (hola/asgi.py)
FECHA: 02-09-2024
VERSION: 3.0
'''


"""
ASGI config for hola project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

# Importaciones externas de Python.
import os

# Importaciones externas de Django.
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hola.settings') # Establece la configuración de Django.

application = get_asgi_application() # Obtiene la aplicación ASGI de Django.
