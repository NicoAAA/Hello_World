'''
SENA CBA CENTRO DE BIOTECNOLOGIA AGROPECUARIA
PROGRAMACION DE SOFTWARE

FICHA: 2877795
AUTOR: NICOLAS ANDRES ACOSTA HIGUERA
PROYECTO: HOLA_MUNDO DJANGO (holass/urls.py)
FECHA: 02-09-2024
VERSION: 3.0
'''


# Importaciones externas de Django.
from django.urls import path

# Importaciones locales.
from holass.views import HomePageView


# Rutas de la aplicación.
urlpatterns = [
    path('', HomePageView.as_view(), name='hola'), # Ruta de la página de inicio.
]