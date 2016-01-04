#!/usr/bin/python
from string import Template

templates = {}

templates['inicio'] = '''
    <html>
        <head>
            <title>${titulo}</title>
        </head>
        <body>
'''

templates['fin'] = '''
        </body>
    </html>
'''

templates['h1'] = '''
            <h1>H1: ${cuerpo}</h1>
            <p>${cuerpito}</p>
'''

templates['h3'] = '''
            <h3>H3: ${cuerpo}</h3>
'''

def generar_ficha(mapa):
    salida = ''
    for seccion in mapa:
        salida = salida + Template(templates[seccion[0]]).substitute(seccion[1])
    return salida