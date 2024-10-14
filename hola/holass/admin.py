'''
SENA CBA CENTRO DE BIOTECNOLOGIA AGROPECUARIA
PROGRAMACION DE SOFTWARE

FICHA: 2877795
AUTOR: NICOLAS ANDRES ACOSTA HIGUERA
PROYECTO: HOLA_MUNDO DJANGO (holass/admin.py)
FECHA: 02-09-2024
VERSION: 3.0
'''

# Importaciones externas de Django.
from django.contrib import admin

# Importaciones locales.
from .models import Post

# Register your models here.

admin.site.register(Post) # Registra el modelo Post en el administrador de Django.