# jekyll - html templating in python

**jekyll_templates** includes templates and replacement function.

**fichas.json** contains the output map.

**jekyll** does the heavy lifting.


| template     | parameters                                                                                         |
|--------------|----------------------------------------------------------------------------------------------------|
| inicio       | titulo, color_primario, color_secundario, color_caracteristica                                     |
| cabecera     | nombre_producto, subtitulo_cabecera, logo_lenovo                                                   |
| P            | t_descripcion_principal, p_descripcion_principal                                                   |
| I            | img_apoyo                                                                                          |
| I-I          | img_apoyo_1, img_apoyo_2                                                                           |
| I-P          | img_apoyo, t_caracteristica, p_caracteristica, numero_caracteristica                               |
| I-P-nonumero | img_apoyo, p_caracteristica                                                                        |
| P-I          | img_apoyo, t_caracteristica, p_caracteristica, numero_caracteristica                               |
| P-I-I        | img_apoyo_1, img_apoyo_2, t_caracteristica, p_caracteristica, numero_caracteristica                |
| I-P-I        | img_apoyo_1, img_apoyo_2, t_caracteristica, p_caracteristica, numero_caracteristica                |
| Igrande-P-I  | img_apoyo_1, img_apoyo_2, t_caracteristica, p_caracteristica                                       |
| I-IP-I       | img_apoyo_1, img_apoyo_2, img_apoyo_3, t_caracteristica, p_caracteristica, numero_caracteristica   |
| P-P          | icono_caracteristica_1, icono_caracteristica_2, detalle_caracteristica_1, detalle_caracteristica_2 |
| fin          |                                                                                                    |
