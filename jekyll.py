#!/usr/bin/python
#coding: utf-8

import os
import json
import jekyll_templates

input_json_file = open('fichas.json', 'r')
input_json_data = json.load(input_json_file)
input_json_file.close()

#os.makedirs('output')

for ficha in input_json_data:
    output_html = jekyll_templates.generar_ficha(ficha['mapa'])
    output_html_file = open('cristian_folder/' + ficha['nombre'] + '.html', 'w')
    output_html_file.write(output_html.encode('utf-8'))
    output_html_file.close()
