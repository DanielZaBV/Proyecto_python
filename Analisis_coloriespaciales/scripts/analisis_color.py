# Analisis_coloriespaciales/analyze.py

def read_selected_colors(filename):
    with open(filename, "r") as file:
        data = file.read()
    return list(map(float, data.split(":")))

def denormalize_value(value, width, height):
    norm_x = int(value * width) % 256
    norm_y = int(value * height) % 256
    return norm_x, norm_y

def group_similar_colors(values, width, height, threshold=20):
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
    return round_to * round(color_value / round_to)

def merge_similar_colors(colors, threshold=20):
    merged = {}
    for color in colors:
        rounded_color = tuple(round_color_value(c, round_to=threshold) for c in color)
        if rounded_color in merged:
            merged[rounded_color] += 1
        else:
            merged[rounded_color] = 1
    return merged

def analyze_color_frequency(grouped_colors, width, height, cluster_size=317, threshold=20):
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
