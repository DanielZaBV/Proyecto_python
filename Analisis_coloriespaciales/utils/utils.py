from typing import List

from Analisis_coloriespaciales.scripts.analisis_color import  read_selected_colors, group_similar_colors, analyze_color_frequency

def analyze_colors(filename, width, height):
    """
    Realiza un análisis de la frecuencia de colores en una imagen.

    Parameters:
    - filename (str): Nombre del archivo que contiene los colores seleccionados.
    - width (int): Ancho de la imagen.
    - height (int): Alto de la imagen.

    Returns:
    - dict: Un diccionario que contiene la frecuencia de colores agrupados por clúster.
            El formato del diccionario es: {cluster: {color: frecuencia}}.
    """
    values = read_selected_colors(filename)
    grouped_colors = group_similar_colors(values, width, height)
    color_frequency = analyze_color_frequency(grouped_colors, width, height)

    for cluster, colors in color_frequency.items():
        print(f"Cluster {cluster}:")
        for color, frequency in colors.items():
            print(f"  Color {color}: {frequency} veces")
