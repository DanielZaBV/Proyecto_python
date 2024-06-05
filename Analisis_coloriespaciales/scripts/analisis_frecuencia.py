import numpy as np

def analyze_color_frequency(grouped_colors, width, height, cluster_size=317):
    """
    Analiza la frecuencia de colores en una imagen agrupándolos en clústeres.

    Parameters:
    - grouped_colors (dict): Un diccionario donde las claves son colores (RGB) y los valores
                             son listas de posiciones normalizadas asociadas a esos colores.
    - width (int): Ancho de la imagen.
    - height (int): Alto de la imagen.
    - cluster_size (int, optional): Tamaño de cada clúster en píxeles. Por defecto es 317.

    Returns:
    - dict: Un diccionario que contiene la frecuencia de colores agrupados por clúster.
            El formato del diccionario es: {(cluster_x, cluster_y): {color: frecuencia}}.
    """
    color_frequency = {}

    for color, values in grouped_colors.items():
        for value in values:
            norm_x, norm_y = denormalize_value(value, width, height)
            cluster_x = int(norm_x // cluster_size)
            cluster_y = int(norm_y // cluster_size)
            cluster_key = (cluster_x, cluster_y)

            if cluster_key not in color_frequency:
                color_frequency[cluster_key] = {}

            if color not in color_frequency[cluster_key]:
                color_frequency[cluster_key][color] = 0

            color_frequency[cluster_key][color] += 1

    return color_frequency

def denormalize_value(value, width, height):
    """
    Convierte un valor normalizado en coordenadas de píxel en una imagen.

    Parameters:
    - value (float): El valor normalizado (0 a 1) que representa la posición.
    - width (int): El ancho de la imagen.
    - height (int): El alto de la imagen.

    Returns:
    - tuple: Una tupla (norm_x, norm_y) donde norm_x es la posición x denormalizada y norm_y es la posición y denormalizada.
    """
    norm_x = value * width
    norm_y = value * height
    return norm_x, norm_y
