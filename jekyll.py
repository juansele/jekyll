#!/usr/bin/python
import os
import json
import jekyll_templates

input_json_file = open('fichas.json', 'r')
input_json_data = json.load(input_json_file)

os.makedirs('output')

for ficha in input_json_data:
    output_html = jekyll_templates.generar_ficha(ficha['mapa'])
    output_html_file = open('output/' + ficha['nombre'] + '.html', 'w')
    output_html_file.write(output_html)
    output_html_file.close()