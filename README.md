# jekyll - html templating in python

**jekyll_templates** includes templates and replacement function.

**fichas.json** contains the output map.

**jekyll** does the heavy lifting.

**output** contains the ...

---

### Template parameters

| template     | parameters                                                                                         |
|--------------|----------------------------------------------------------------------------------------------------|
| inicio       | titulo, color_primario, color_secundario, color_caracteristica                                     |
| cabecera     | nombre_producto, subtitulo_cabecera, logo_lenovo                                                   |
| P            | t_descripcion_principal, p_descripcion_principal                                                   |
| I            | img_apoyo                                                                                          |
| I-I          | img_apoyo_1, img_apoyo_2                                                                           |
| I-P          | img_apoyo, t_caracteristica, p_caracteristica, numero_caracteristica                               |
| I-P-nonumero | img_apoyo, p_caracteristica                                                                        |
| P-I-num_centro          | img_apoyo, t_caracteristica, p_caracteristica, numero_caracteristica                               |
| P-I-num_izq          | img_apoyo, t_caracteristica, p_caracteristica, numero_caracteristica                               |
| P-I-I        | img_apoyo_1, img_apoyo_2, t_caracteristica, p_caracteristica, numero_caracteristica                |
| I-P-I        | img_apoyo_1, img_apoyo_2, t_caracteristica, p_caracteristica, numero_caracteristica                |
| Igrande-P-I  | img_apoyo_1, img_apoyo_2, p_caracteristica                                       |
| I-IP-I       | img_apoyo_1, img_apoyo_2, img_apoyo_3, t_caracteristica, p_caracteristica, numero_caracteristica   |
| P-P          | icono_caracteristica_1, icono_caracteristica_2, detalle_caracteristica_1, detalle_caracteristica_2 |
| fin          |                                                                                                    |


### Fichas color squema

| NOMBRE FICHA                    | COLOR PRIMARIO | COLOR SECUNDARIO | COLOR CARACTERÍSTICA |
|---------------------------------|----------------|------------------|----------------------|
| LENOVO AIO_700                  | 231f20         | 8abf54           | ed6b00               |
| LENOVO B50 30                   | 231f20         | c22821           | ed6b00               |
| LENOVO C40 05                   | 231f20         | c22821           | ed6b00               |
| LENOVO C40 30                   | 231f20         | c22821           | ed6b00               |
| LENOVO C40 30 EXITO             | 231f20         | c22821           | ed6b00               |
| LENOVO C50 30                   | 231f20         | c22821           | ed6b00               |
| LENOVO C260                     | 717170         | 8abf54           | 4a80b0               |
|                                 |                |                  |                      |
| LENOVO G40 30                   | 717170         | ed6b00           | 4a80af               |
| LENOVO G40 45                   | 717170         | ed6b00           | 4a80af               |
| LENOVO G40 80                   | 717170         | ed6b00           | 4a80af               |
| LENOVO IDEAPAD 100              | 717170         | 5e8cda           | 4a80af               |
| LENOVO IDEAPAD 100s 11'' AZUL   | 231f20         | ed6b00           | 4a80af               |
| LENOVO IDEAPAD 100s 11'' BLANCO | 231f20         | ed6b00           | 4a80af               |
| LENOVO IDEAPAD 300              | 231f20         | d06bac           | 4a80af               |
| LENOVO Y50 70                   | 717170         | c22821           | 4a80af               |
| LENOVO Z40 70                   | 717170         | d06bac           | 4a80af               |
| LENOVO Z50 70                   | 717170         | d06bac           | 4a80af               |
|                                 |                |                  |                      |
| LENOVO YOGA 2 13''              | 717170         | c22821           | 4a80af               |
| LENOVO YOGA 3 14''              | 717170         | c22821           | 4a80af               |
| LENOVO YOGA 300 11''            | 717170         | c22821           | 4a80af               |
| LENOVO YOGA 500                 | 717170         | c22821           | 4a80af               |
|                                 |                |                  |                      |
| LENOVO PHAB                     | 6e8dc4         | 8abf54           | 4a80af               |
| LENOVO TAB2 A7 10 + BOUNDLE     | ed6b00         | c22821           | 4a80af               |
| LENOVO TAB2 A7 10               | ed6b00         | c22821           | 4a80af               |
| LENOVO TAB2 A7 20               | ed6b00         | c22821           | 4a80af               |
| LENOVO TAB2 A7 30               | ed6b00         | c22821           | 4a80af               |
| LENOVO YOGA TABLET 3 8"         | 8dc1e1         | d07100           | 4a80af               |
| YOGA TABLET 2 10’’ 4G           | 6e8dc4         | c22821           | 4a80af               |
| YOGA TABLET 2 10’’              | 6e8dc4         | c22821           | 4a80af               |
| YOGA TABLET 2 13’’              | 4981b9         | c22821           | 4a80af               |
