def read_selected_colors(filename):
    """
    Lee un archivo de texto que contiene valores normalizados de colores seleccionados y los convierte en una lista de flotantes.

    Parameters:
    - filename (str): El nombre del archivo que contiene los valores normalizados de colores, separados por dos puntos (:).

    Returns:
    - list: Una lista de valores de color normalizados como flotantes.
    """
    with open(filename, "r") as file:
        data = file.read()
    return list(map(float, data.split(":")))

def denormalize_value(value, width, height):
    """
    Convierte un valor normalizado en coordenadas de píxel en una imagen y las ajusta para que estén en el rango de 0 a 255.

    Parameters:
    - value (float): El valor normalizado (0 a 1) que representa la posición.
    - width (int): El ancho de la imagen.
    - height (int): El alto de la imagen.

    Returns:
    - tuple: Una tupla (norm_x, norm_y) donde norm_x y norm_y son las posiciones denormalizadas y ajustadas al rango de 0 a 255.
    """
    norm_x = int(value * width) % 256
    norm_y = int(value * height) % 256
    return norm_x, norm_y

def group_similar_colors(values, width, height, threshold=20):
    """
    Agrupa colores similares en clústeres basados en una posición normalizada y un umbral.

    Parameters:
    - values (list): Lista de valores normalizados que representan posiciones de colores.
    - width (int): Ancho de la imagen.
    - height (int): Alto de la imagen.
    - threshold (int, optional): Umbral para agrupar colores similares. Por defecto es 20.

    Returns:
    - dict: Un diccionario donde las claves son tuplas que representan clústeres (cluster_x, cluster_y)
            y los valores son listas de valores normalizados asociados a esos clústeres.
    """
    grouped_colors = {}
    for val in values:
        norm_x, norm_y = denormalize_value(val, width, height)
        cluster_x, cluster_y = int(norm_x // 317), int(norm_y // 317)
        color_key = (cluster_x, cluster_y)

        if color_key not in grouped_colors:
            grouped_colors[color_key] = []
        grouped_colors[color_key].append(val)
    return grouped_colors

def round_color_value(color_value, round_to=20):
    """
    Redondea un valor de color al múltiplo más cercano de un valor especificado.

    Parameters:
    - color_value (int): El valor de color que se va a redondear.
    - round_to (int, optional): El múltiplo al que se redondeará el valor de color. Por defecto es 20.

    Returns:
    - int: El valor de color redondeado al múltiplo más cercano de `round_to`.
    """
    return round_to * round(color_value / round_to)

def merge_similar_colors(colors, threshold=20):
    """
    Agrupa y cuenta colores similares basados en un umbral especificado.

    Parameters:
    - colors (list): Lista de tuplas que representan los valores RGB de los colores.
    - threshold (int, optional): Umbral para agrupar colores similares. Por defecto es 20.

    Returns:
    - dict: Un diccionario donde las claves son los colores redondeados a los múltiplos más cercanos del umbral,
            y los valores son la cantidad de veces que cada color aparece en la lista original.
    """
    merged = {}
    for color in colors:
        rounded_color = tuple(round_color_value(c, round_to=threshold) for c in color)
        if rounded_color in merged:
            merged[rounded_color] += 1
        else:
            merged[rounded_color] = 1
    return merged

def analyze_color_frequency(grouped_colors, width, height, cluster_size=317, threshold=20):
    """
    Analiza la frecuencia de colores agrupados en clústeres basados en un tamaño de clúster y un umbral especificado.

    Parameters:
    - grouped_colors (dict): Diccionario donde las claves son tuplas que representan clústeres (cluster_x, cluster_y)
                             y los valores son listas de valores normalizados asociados a esos clústeres.
    - width (int): Ancho de la imagen.
    - height (int): Alto de la imagen.
    - cluster_size (int, optional): Tamaño de cada clúster en píxeles. Por defecto es 317.
    - threshold (int, optional): Umbral para agrupar colores similares. Por defecto es 20.

    Returns:
    - dict: Un diccionario donde las claves son las coordenadas de los clústeres (cluster_x, cluster_y)
            y los valores son diccionarios de frecuencias de colores agrupados.
    """
    color_frequency = {}

    for key, values in grouped_colors.items():
        cluster_x, cluster_y = key
        cluster_key = (cluster_x, cluster_y)
        
        colors = []
        for value in values:
            norm_x, norm_y = denormalize_value(value, width, height)
            color = (int(norm_x), int(norm_y), int(norm_x))  # Suponiendo valor RGB igual para simplificación
            colors.append(color)
        
        merged_colors = merge_similar_colors(colors, threshold)
        
        color_frequency[cluster_key] = merged_colors
    
    return color_frequency
