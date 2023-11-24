import os
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM

# Caminho para o arquivo SVG de entrada
input_svg = 'static/vector/generated_image.svg'

# Caminho para o arquivo PNG de saída
output_png = 'static/brand-content/generated_image.png'

# Converte o arquivo SVG para um objeto ReportLab Graphics
drawing = svg2rlg(input_svg)

# Calcula as novas dimensões mantendo a proporção
largura_original = drawing.width
altura_original = drawing.height
nova_largura = 300
nova_altura = int((altura_original / largura_original) * nova_largura)

# Redimensiona o desenho
drawing.width = nova_largura
drawing.height = nova_altura

# Renderiza o desenho em um arquivo PNG
renderPM.drawToFile(drawing, output_png, fmt="PNG")

print(f'A imagem foi convertida para PNG, redimensionada e salva em {output_png}')
