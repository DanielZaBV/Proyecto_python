import numpy as np

def analyze_color_frequency(grouped_colors, width, height, cluster_size=317):
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
    norm_x = value * width
    norm_y = value * height
    return norm_x, norm_y
